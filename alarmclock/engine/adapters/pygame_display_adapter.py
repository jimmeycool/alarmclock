import pygame
from pygame import Surface
from PIL import Image
from typing import Tuple
from config.models import DeviceConfig
from .display_adapter import DisplayAdapter

class PyGameDisplayAdapter(DisplayAdapter):
  display_width = 128
  display_height = 128
  display_grid = (0, 0)
  window = None

  def __init__(self, device_config: DeviceConfig) -> None:
    """
    Creats a PyGame display adapter

    Args:
        device_config (DeviceConfig):  Config on how to setup this device
    """
    super().__init__((self.display_width, self.display_height))
    
    if not pygame.get_init():
      pygame.init()

    self.location = device_config.location
  
    PyGameDisplayAdapter.display_grid = self.new_display_grid()
    PyGameDisplayAdapter.window = self.new_window()

  def update(self, image: Image):
    pygame.event.get() # hack, needed
    surface = self.image_to_surface(image)
    self.window.blit(surface, (self.location[0] * self.display_width, self.location[1] * self.display_height))
    pygame.display.flip()

  def new_display_grid(self) -> Tuple[int, int]:
    """
    Creates a tuple represeting the dimensions of the grid of displays,
    implied by all existing PyGameDisplayAdapter_s.

    Returns:
        Tuple[int, int]: a tuple represetings the dimensions of the display grid.
    """
    return tuple([max(*l) for l in zip(self.location, self.display_grid)])

  def new_window(self) -> Surface:
    """_summary_
    Creates a Surface matching the combined dimensions of the grid of displays.

    Returns:
        Surface: A new Surface with dimensions that match the latest display_grid
    """
    return pygame.display.set_mode([
      (self.display_grid[0] + 1) * self.display_width,
      (self.display_grid[1] + 1) * self.display_height,
    ])

  def image_to_surface(self, image: Image) -> Surface:
    """
    Converts an Image into a Surface.

    Args:
        image (Image): PIL image

    Returns:
        Surface: PyGame Surface corresponding to the PIL image
    """
    return pygame.image.fromstring(
      image.tobytes(), image.size, image.mode).convert()

