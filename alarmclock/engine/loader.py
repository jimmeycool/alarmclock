import importlib
from typing import Any, Dict, List, Tuple

from config import DeviceConfig, ScreenConfig
from .components import ViewModule, RenderModule
from .adapters import DisplayAdapter, PyGameDisplayAdapter, SSD1351DisplayAdapter


def load(device_configs: List[DeviceConfig], screen_configs: List[ScreenConfig]) -> List[RenderModule]:
    """
    Load in the devices, view modules, and tie them together into a 
    list of render modules

    Args:
        device_configs (List[DeviceConfig]): List of available devices
        screen_configs (List[ScreenConfig]): List of the screen configurations

    Returns:
        List[RenderModule]: List of render objects
    """
    adapters = {str(config.location):_load_adapter(config) for config in device_configs}
    return [_load_renderer(adapters, config) for config in screen_configs]

def _load_adapter(config: DeviceConfig) -> DisplayAdapter:
    """
    Creates a ready connection to te given screen with the given SPI 
    config.

    Args:
        config (Config): Config of screen to connect

    Returns:
        device: Active device to draw on
    """

    if config.display == 'pygame':
        # Use default size for now
        return PyGameDisplayAdapter((128, 128))
    
    if config.display == 'ssd1351':
        return SSD1351DisplayAdapter(config)

    raise Exception(f'Cannot find a matching adapter for {config.display}')

def _load_renderer(adapters: Dict[str, DisplayAdapter], screen_config: ScreenConfig) -> RenderModule:
    """
    Loads a render module from the given set of adapters, and a screen config

    Args:
        adapters (Dict[Tuple[int, int]], DisplayAdapter): Dictionary of available adapters
        screen_config (ScreenConfig): Screen to make renderer of

    Returns:
        RenderModule: Active render object for the screen
    """
    view_module = _load_view_module(screen_config.view_module, screen_config.config)
    display_adapter = adapters.get(str(screen_config.location))
    return RenderModule(display_adapter, view_module)

def _load_view_module(name: str, config: Any = None) -> ViewModule:
  """
  Dynamically loads a view module by name.

  Args:
      name (str): The name of the view module to load.
      config (Any, optional): Configuraion for the view module. Defaults to None.

  Returns:
      ViewModule: The dynamically loaded view module.
  """
  module = importlib.import_module(f".view_modules.{name}", package='alarmclock')
  return ViewModule(module.Controller(config), module.View(config), config)