import os
import yaml
from typing import List

from .models import SpiConfig, ScreenConfig

spi_config: SpiConfig
'''
Config of device SPI ports/settings
'''

screen_configs: List[ScreenConfig]
'''
List of screens avaliable with config settings
'''

with open(os.path.join('config','devices.yml')) as file:
    screen_configs = yaml.unsafe_load(file)

with open(os.path.join('config','spi.yml')) as file:
    spi_config = yaml.safe_load(file)