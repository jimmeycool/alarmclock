
from typing import List

from config import DeviceConfig, ScreenConfig

from .loader import load


def start(device_configs: List[DeviceConfig], screen_configs: List[ScreenConfig]):
    """
    Starts the alarm clock!

    Args:
        device_configs (List[DeviceConfig]): List of avalible devices to load in and use
        screen_configs (List[ScreenConfig]): List of screens to show
    """
    renderers = load(device_configs, screen_configs)
    try:
        while True:
            _ = [r.execute() for r in renderers]
    except Exception as ex:
        _ = [r.cleanup() for r in renderers]
        raise ex