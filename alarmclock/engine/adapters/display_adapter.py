from abc import ABC, abstractmethod
from PIL import Image
from typing import Tuple

class DisplayAdapter(ABC):

  def __init__(self, dimensions: Tuple[int, int]) -> None:
    """
    Creates a new display adapter instance.

    Args:
        dimensions (Tuple[int, int]): The display dimensions
    """
    super().__init__()
    self.dimensions = dimensions

  @abstractmethod
  def  update(self, image: Image) -> None:
    """
    Pushes the given image to the display.

    Args:
        image (Image): The image to be displayed.
    """
    pass

  def cleanup():
    """
    Perform any cleanup that is needed if we need
    to end connection
    """
    pass
