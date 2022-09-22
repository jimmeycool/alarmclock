from alarmclock.engine.components import ViewBase
from PIL import Image, ImageDraw
from typing import Any, Tuple
import datetime

class View(ViewBase):

  def draw(self, dimensions: Tuple[int, int], model: Any = None) -> Image:
    image = Image.new("RGB", dimensions, (0, 0, 0))
    draw = ImageDraw.Draw(image)
    now = datetime.datetime.now()
    hours_text = str(now.hour).zfill(2)
    draw.text(model, hours_text)
    return image
