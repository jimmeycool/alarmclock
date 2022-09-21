import yaml
from typing import Tuple


class SpiConfig(yaml.YAMLObject):
    yaml_loader = yaml.SafeLoader
    yaml_tag = u'!SpiConfig'

    def __init__(self, clock_pin: int, mosi_pin: int, miso_pin: int):
        """
        Config file for the SPI settings

        Args:
            clock_pin (int): Clock pin
            mosi_pin (int): MOSI pin
            miso_pin (int): MISO pin
        """
        self.clock_pin = clock_pin
        self.mosi_pin = mosi_pin
        self.miso_pin = miso_pin

class ScreenConfig(yaml.YAMLObject):
    yaml_loader = yaml.UnsafeLoader
    yaml_tag = u'!ScreenConfig'

    def __init__(self, location: Tuple[int, int], name: str, width: int, height: int, reset_pin: int, cs_pin: int, dc_pin: int, device: str):
        """
        Config class for a screen, define how we are going to connect to it and
        other metadat

        Args:
            location (Tuple[int, int]): Location of screen (row, col)
            name (str): Name of screen
            width (int): Width of screen
            height (int): Height of screen
            reset_pin (int): Reset pin for screen
            cs_pin (int): Chip select pin for screen
            dc_pin (int): Device Control pin for screen
            device (str): Type of device
        """
        self.location = location
        self.name = name
        self.width = width
        self.height = height
        self.reset_pin = reset_pin
        self.cs_pin = cs_pin
        self.dc_pin = dc_pin
        self.device = device
