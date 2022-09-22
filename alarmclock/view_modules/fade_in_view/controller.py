from typing import Any
import timeit
from alarmclock.engine.components import ControllerBase

class Controller(ControllerBase):
  fade_duration = 1

  def __init__(self, config: Any = None) -> None:
    super().__init__(config)
    self.start_time = timeit.default_timer()
    self.color = tuple(config["color"])

  def update(self) -> Any:
    elasped_time = timeit.default_timer() - self.start_time
    if (elasped_time < self.fade_duration):
      # interpolate from black to target color
      ratio = elasped_time / self.fade_duration
      return tuple([int(ratio * value) for value in self.color])

    return self.color
