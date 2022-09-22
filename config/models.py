import yaml
from typing import Any, Tuple

class DeviceConfig(yaml.YAMLObject):
    yaml_loader = yaml.UnsafeLoader
    yaml_tag = u'!DeviceConfig'

    def __init__(
        self,
        location: Tuple[int, int],
        name: str,
        display: str,
        gpio_reset: int = None,
        gpio_chip_select: int = None,
        gpio_dc: str = None,
        port: int = None):
        """
        Config class for a screen, define how we are going to connect to it and
        other metadata

        Args:
            location (Tuple[int, int]): Location in the clock (row, col)
            name (str): Name of display
            display (str): Display type
            gpio_reset (int): Reset pin
            gpio_chip_select (int): CS pin
            gpio_dc (str): DC pin
            port (int): SPI port (0 or 1)
        """
        self.location = location
        self.name = name
        self.display = display
        self.gpio_reset = gpio_reset
        self.gpio_chip_select = gpio_chip_select
        self.gpio_dc = gpio_dc
        self.port = port


class ScreenConfig(yaml.YAMLObject):
    yaml_loader = yaml.UnsafeLoader
    yaml_tag = u'!ScreenConfig'

    def __init__(self, location: Tuple[int, int], view_module: str, config: Any = None):
        """
        Config for setting up the MVC componets for the clock

        Args:
            location (Tuple[int, int]): Position of module
            view_module (str): Name of view module
            config (Any, optional): Config object for the module. Defaults to None.
        """
        self.location = location
        self.view_module = view_module
        self.config = config
        