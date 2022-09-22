import os
import yaml
from typing import List

from .models import DeviceConfig, ScreenConfig

device_configs: List[DeviceConfig]
'''
List of screens available with config settings
'''

screen_configs = List[ScreenConfig]
'''
List of screen configs
'''

# Use "UnsafeLoader" to allow the use of python types

with open(os.path.join('config','devices.yml')) as file:
    device_configs = yaml.unsafe_load(file)

with open(os.path.join('config','screens.yml')) as file:
    screen_configs = yaml.unsafe_load(file)