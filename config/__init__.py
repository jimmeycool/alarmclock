import os
import yaml
from typing import List

from .models import ScreenConfig

screen_configs: List[ScreenConfig]
'''
List of screens avaliable with config settings
'''

with open(os.path.join('config','devices.yml')) as file:
    screen_configs = yaml.unsafe_load(file)
