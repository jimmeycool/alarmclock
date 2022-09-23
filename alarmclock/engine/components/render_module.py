from datetime import datetime, timedelta
from distutils.command.config import config
from typing import List
from PIL import Image


from  .view_container import ViewContainer
from .image_cache import ImageCache
from ..adapters import DisplayAdapter

class RenderModule:

    def __init__(self, display_adapter: DisplayAdapter, view_containers: List[ViewContainer]):
        """
        Class for tieing the view module with the location

        Args:
            display_adapter (Tuple[int, int]): Adapter to render image
            view_module (ViewModule): View Module to render
        """
        self.display_adapter = display_adapter
        self.image_cache = ImageCache()

        self._dimensions = display_adapter.dimensions
        self._view_containers = view_containers
        self._last_switch_time = datetime.now()

    def execute(self) -> Image:
        """
        Executes this render module and return image

        Returns:
            Image: Latest image to return 
        """
        view_container = self._get_current()
        return self._render_view_container(view_container)

    def _get_current(self):
        """
        Gets the current view container
        """
        current = self._view_containers[0]
        seconds = current.config.duration_sec if hasattr(current.config, 'duration_sec') else None
        if seconds and (datetime.now() - self._last_switch_time) >= timedelta(seconds=seconds):
            return self._get_next(current)
        return current

    def _get_next(self, current: ViewContainer):
        """
        Gets the next view container
        """
        self._last_switch_time = datetime.now()
        if len(self._view_containers) == 1:
            return current

        self._view_containers.pop(0)

        if not current.config.onetime:
            self._view_containers.append(current)
        
        return self._view_containers[0]

    def cleanup(self):
        """
        Perform any cleanup that is needed
        """
        self.display_adapter.cleanup()

    def _render_view_container(self, view_container: ViewContainer) -> Image:
        """
        Renders the view container into an image

        Args:
            view_container (ViewContainer): View Container to show

        Returns:
            Image: Resulting image
        """
        view_module = view_container.view_module
        model = view_module.controller.update()
        image = view_module.view.draw(self._dimensions, model)
        if self.image_cache.cache_if_changed(image):
            self.display_adapter.update(image)