from PIL import Image, ImageDraw

from .view_module import ViewModule
from ..adapters import DisplayAdapter

class RenderModule:

    def __init__(self, display_adapter: DisplayAdapter, view_module: ViewModule):
        """
        Class for tieing the view module with the location

        Args:
            display_adapter (Tuple[int, int]): Adapter to render image
            view_module (ViewModule): View Module to render
        """
        self.display_adapter = display_adapter
        self.view_module = view_module
        self._dimensions = display_adapter.dimensions

    def execute(self) -> Image:
        """
        Executes this render module and return image

        Returns:
            Image: Latest image to return 
        """

        model = self.view_module.controller.update()
        image = self.view_module.view.draw(self._dimensions, model)
        self.display_adapter.update(image)


