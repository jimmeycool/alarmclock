from typing import Any
from alarmclock.engine.components import ControllerBase

class Controller(ControllerBase):

  def __init__(self, config: Any = None) -> None:
    super().__init__(config)

  def update(self) -> Any:
    pass
