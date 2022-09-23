from datetime import datetime, timedelta
import math
from random import random
from alarmclock.engine.components import ViewBase
from PIL import Image, ImageDraw
from typing import Any, Tuple

import numpy as np
import scipy as sp
from scipy.interpolate import interp1d
from dateutil import parser

from alarmclock.view_modules.utilities import get_arial_font

class View(ViewBase):

  def draw(self, dimensions: Tuple[int, int], model: Any = None) -> Image:
    image = Image.new("RGB", dimensions, (0, 0, 0))
    if model.data == None:
      return image

    draw = ImageDraw.Draw(image)

    y = model.data
    x = list(range(0, len(model.data)))

    new_length = 128
    new_x = np.linspace(min(x), max(x), new_length)
    new_y = sp.interpolate.interp1d(x, y, kind='cubic')(new_x)

    for i in range(len(new_x)):
      value = new_y[i]
      start = i
      end = start + 1
      draw.rectangle((
        start,
        dimensions[1],
        end,
        dimensions[1] - value
      ), fill="red")

    font = get_arial_font(10)
    draw.multiline_text((5, 5), f"High: {max(y)}°F\nLow: {min(y)}°F", font=font)

    font = get_arial_font(8)
    time = datetime.now()
    for i in range(0, 4):
      hour_str = f"{time.strftime('%I%p')}"
      draw.text(((128 / 4) * i, 110), hour_str, font=font)
      time = time + timedelta(hours=6)

    return image
