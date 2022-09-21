import asyncio
import time

from abc import abstractmethod
from dataclasses import dataclass
from typing import Any

from controller import ControllerBase

@dataclass
class AsyncModel:
  is_loading: bool
  is_error: bool
  data: Any

class AsyncControllerBase(ControllerBase):

  def __init__(self, config: Any) -> None:
    """
    Creates a new async controller instance.

    Args:
        config (Any): The configuration for this controller, should contain last_refresh_time.
    """
    super().__init__(config)
    self.last_refresh_time = None
    self.model = AsyncModel(True, False, None)

  def due_for_refresh(self) -> bool:
    return time.time() - self.last_refresh_time >= self.config.refresh_interval_seconds

  def update(self) -> Any:
    if self.last_refresh_time is None or self.due_for_refresh():
      self.last_refresh_time = time.time()
      asyncio.run(self.fetch())
    
    return self.model
  
  @abstractmethod
  async def fetch(self) -> None:
    """
    Perform asynchronous actions and update self.model.
    """
    pass
