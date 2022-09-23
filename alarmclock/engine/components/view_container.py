from config import ModuleConfig

from .view_module import ViewModule

class ViewContainer:

    def __init__(self, config: ModuleConfig, view_module: ViewModule) -> None:
        """
        Active view module with its config for screen rendering

        Args:
            config (ModuleConfig): Config for rendering this screen
            view_module (ViewModule): View Module
        """
        self.config = config
        self.view_module = view_module