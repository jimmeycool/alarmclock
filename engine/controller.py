from abc import ABC, abstractmethod
from typing import Any

class Controller(ABC):

  def __init__(self, config: Any = None) -> None:
    """
    Creates a new controller instance.

    Args:
        config (Any, optional):The configuration for this controller. Defaults to None.
    """
    super().__init__()
    self.config = config

  @abstractmethod
  def update(self) -> Any:
    """
    Updates this controller's model and returns the result. Called once per tick.

    Returns:
        Any: The model associated with this controller.
    """
    pass
