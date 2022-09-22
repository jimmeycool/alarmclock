from alarmclock.engine.components import ViewBase
from PIL import ImageDraw
from typing import Any

class View(ViewBase):

  def draw(self, draw: ImageDraw, model: Any = None) -> None:
    draw.rectangle([(0, 0), (128, 128)], fill=model)
