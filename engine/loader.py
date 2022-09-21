import importlib
from typing import Any, Dict, List, Tuple
from luma.core.interface.serial import gpio_cs_spi
from luma.oled.device import device, ssd1351

from config.models import DeviceConfig, ScreenConfig
from components import ViewModule


def load(device_configs: List[DeviceConfig], screen_configs: List[ScreenConfig]):
    devices = load_devices(device_configs)
    screens = load_screens(screen_configs)

def load_screens(screen_configs: List[ScreenConfig]):
    pass

def load_devices(device_configs: List[DeviceConfig]) -> Dict[Tuple[int, int], device]:
    """
    Creates a mapping of locations to active screen devices

    Args:
        configs (List[ScreenConfig]): List of screen configs

    Returns:
        Dict[Tuple[int, int], device]: Mapping of location (x,y) to screen (device)
    """
    return {config.location:_load_device(config) for config in device_configs}

def _load_device(screen_config: DeviceConfig) -> device:
    """
    Creates a ready connection to te given screen with the given SPI 
    config. Only supports SDD1351 displays at the moment

    Args:
        spi_config (SpiConfig): SPI config
        screen_config (ScreenConfig): Config of screen to connect

    Returns:
        device: Active device to draw on
    """
    spi = gpio_cs_spi(
        port=screen_config.port,
        gpio_cs=screen_config.gpio_chip_select,
        gpio_dc=screen_config.gpio_dc,
        gpio_RST= screen_config.gpio_reset
    )

    return ssd1351(serial_interface=spi)

def load_view_module(name: str, config: Any = None) -> ViewModule:
  """
  Dynamically loads a view module by name.

  Args:
      name (str): The name of the view module to load.
      config (Any, optional): Configuraion for the view module. Defaults to None.

  Returns:
      ViewModule: The dynamically loaded view module.
  """
  module = importlib.import_module(f"view_modules.{name}")
  return ViewModule(module.Controller(config), module.View(config), config)