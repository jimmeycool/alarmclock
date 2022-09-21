import yaml
from typing import Tuple

class ScreenConfig(yaml.YAMLObject):
    yaml_loader = yaml.UnsafeLoader
    yaml_tag = u'!ScreenConfig'

    def __init__(self, location: Tuple[int, int], name: str, display: str, gpio_reset: int, gpio_chip_select: int, gpio_dc: str, port: int):
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
        self.dispay = display
        self.gpio_reset = gpio_reset
        self.gpio_chip_select = gpio_chip_select
        self.gpio_dc = gpio_dc
        self.port = port
