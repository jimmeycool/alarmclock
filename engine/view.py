from abc import ABC, abstractmethod
from PIL import ImageDraw
from typing import Any

class View(ABC):

  def __init__(self, config: Any = None) -> None:
    """
    Creates a new view instance.

    Args:
        config (Any, optional):The configuration for this view. Defaults to None.
    """
    super().__init__()
    self.config = config

  @abstractmethod
  def draw(self, draw: ImageDraw, model: Any = None) -> None:
    """
    Produces the current view as an image via the drawing interface.

    Args:
        draw (ImageDraw): The drawing interface.
        model (Any, optional): The model associated with this view. Defaults to None.
        config (Any, optional): The configuration associated with this view. Defaults to None.
    """
    pass
