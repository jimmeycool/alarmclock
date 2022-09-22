from alarmclock.engine.components import ViewBase
from PIL import Image, ImageDraw, ImageFont
from typing import Any, Tuple
import datetime

class View(ViewBase):

  def draw(self, dimensions: Tuple[int, int], model: Any = None) -> Image:
    image = Image.new("RGB", dimensions, (0, 0, 0))
    draw = ImageDraw.Draw(image)
    time_part = self.get_time_part()
    text = str(time_part).zfill(2)[0:2]
    font = ImageFont.truetype("arial.ttf", 90)
    size = font.getbbox(text, anchor='lt')
    draw.text(
      (
        (dimensions[0] - size[2]) / 2, 
        (dimensions[1] - size[3]) / 2
      ), 
      text, 
      font=font,
      anchor="lt")
    
    return image

  def get_time_part(self):
    now = datetime.datetime.now()
    interval = self.config["time_part"]
    if interval == "hour":
      return now.hour
    elif interval == "minute":
      return now.minute
    elif interval == "second":
      return now.second
    elif interval == "microsecond":
      return now.microsecond