from typing import Any
from alarmclock.engine.components import ControllerBase
import datetime
import random
import math

class Controller(ControllerBase):
  def __init__(self, config: Any = None) -> None:
    super().__init__(config)
    angle = random.uniform(0, 2.0 * math.pi)
    self.direction = [math.cos(angle), math.sin(angle)]
    self.position = (64, 64)

  def update(self) -> Any:
    if self.position[0] > 120 or self.position[0] <= 0:
      self.direction[0] *= -1
    if self.position[1] > 120 or self.position[1] <= 0:
      self.direction[1] *= -1

    self.position = (
      self.position[0] + self.direction[0],
      self.position[1] + self.direction[1],
    )

    return self.position
