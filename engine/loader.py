from typing import Dict, List, Tuple
from luma.core.interface.serial import gpio_cs_spi
from luma.oled.device import device, ssd1351

from config.models import ScreenConfig

def load_screens(configs: List[ScreenConfig]) -> Dict[Tuple[int, int], device]:
    """
    Creates a mapping of locations to active screen devices

    Args:
        configs (List[ScreenConfig]): List of screen configs

    Returns:
        Dict[Tuple[int, int], device]: Mapping of location (x,y) to screen (device)
    """
    return {config.location:_load_screen(config) for config in configs}

def _load_screen(screen_config: ScreenConfig) -> device:
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

