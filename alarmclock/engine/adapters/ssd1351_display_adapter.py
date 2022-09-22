from PIL import Image

from luma.oled.device import ssd1351
from luma.core.interface.serial import gpio_cs_spi

from .display_adapter import DisplayAdapter
from config import DeviceConfig

class SSD1351DisplayAdapter(DisplayAdapter):
    width = 128
    height = 128

    def __init__(self, device_config: DeviceConfig):
        """
        Create a SSD1351 Display adapter

        Args:
            device_config (DeviceConfig): Config on how to setup this device
        """
        super().__init__((self.width, self.height))
        
        spi = gpio_cs_spi(
            port=device_config.port,
            gpio_cs=device_config.gpio_chip_select,
            gpio_dc=device_config.gpio_dc,
            gpio_RST= device_config.gpio_reset
        )

        self.device = ssd1351(serial_interface=spi)

    def update(self, image: Image) -> None:
        """
        Display the given image

        Args:
            image (Image): Image to display
        """
        self.device.display(image)