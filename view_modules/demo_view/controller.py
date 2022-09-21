from typing import Any
from engine import ControllerBase

class Controller(ControllerBase):

  def __init__(self, config: Any = None) -> None:
    super().__init__(config)
    self.rgb_index = 0
    self.color = [255, 0, 0]

  def update(self) -> Any:
    sub_index = self.rgb_index
    add_index = (sub_index + 1) % 3
    self.color[sub_index] -= 1
    self.color[add_index] += 1
    if self.color[self.rgb_index] == 0:
      self.rgb_index = add_index

    return tuple(self.color)
