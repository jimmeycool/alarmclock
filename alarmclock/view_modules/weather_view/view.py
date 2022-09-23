from alarmclock.engine.components import ViewBase
from PIL import Image, ImageDraw, ImageFont
from typing import Any, Tuple
import time
import datetime

from dateutil import parser

from alarmclock.view_modules.utilities import get_arial_font

class View(ViewBase):

  def draw(self, dimensions: Tuple[int, int], model: Any = None) -> Image:
    image = Image.new("RGB", dimensions, (0, 0, 0))
    if model == None:
      return image

    horiz_margin = int((dimensions[0] - model.image.width) / 2)
    vert_margin = int((dimensions[1] - model.image.height) / 2)

    image.paste(model.image, (horiz_margin, vert_margin))


    time = parser.parse(model.time)
    hourMinute_str = f"{time.strftime('%I:%M %p')} {model.temp}° F"
    bottom_text = model.desc
    
    font = get_arial_font(15)
    size = font.getbbox(hourMinute_str, anchor='lt')
    draw = ImageDraw.Draw(image)
    draw.text(
      (
        (dimensions[0] - size[2]) / 2, 
        (vert_margin - size[3]) / 2
      ), 
      hourMinute_str, 
      font=font,
      anchor="lt")
    size = font.getbbox(bottom_text, anchor='lt')
    draw.text(
      (
        (dimensions[0] - size[2]) / 2, 
        vert_margin + model.image.height + (vert_margin - size[3]) / 2
      ), 
      bottom_text, 
      font=font,
      anchor="lt")
    
    return image

