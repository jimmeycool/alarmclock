from dataclasses import dataclass
from typing import Any
import timeit
from alarmclock.engine.components import ControllerBase

@dataclass
class Model:
  percent_progress: float

class Controller(ControllerBase):
  fade_duration = 3

  def __init__(self, config: Any = None) -> None:
    super().__init__(config)
    self.start_time = timeit.default_timer()
    self.color = tuple(config["color"])

  def update(self) -> Any:
    elasped_time = timeit.default_timer() - self.start_time
    percent_progress = min(elasped_time / self.fade_duration, 1)
    return Model(percent_progress)
