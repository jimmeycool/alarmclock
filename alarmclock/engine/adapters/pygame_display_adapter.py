import pygame
from pygame import Surface
from PIL import Image
from .display_adapter import DisplayAdapter

class PyGameDisplayAdapter(DisplayAdapter):
  def __init__(self, dimensions) -> None:
    super().__init__(dimensions)
    pygame.init()

    self.window = pygame.display.set_mode(dimensions)

  def update(self, image: Image):
    pygame.event.get() # hack, needed
    surface = self.image_to_surface(image)
    self.window.blit(surface, (0, 0))
    pygame.display.flip()

  def image_to_surface(self, image: Image) -> Surface:
    return pygame.image.fromstring(
      image.tobytes(), image.size, image.mode).convert()
