from alarmclock.engine.components import ViewBase
from PIL import ImageDraw
from typing import Any
import datetime

class View(ViewBase):

  def draw(self, draw: ImageDraw, model: Any = None) -> None:
    now = datetime.datetime.now()
    hours_text = str(now.hour).zfill(2)
    draw.text(model, hours_text)
