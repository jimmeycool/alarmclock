from alarmclock.engine.components import ViewBase
from PIL import Image, ImageDraw
from typing import Any, Tuple

class View(ViewBase):

  def draw(self, dimensions: Tuple[int, int], model: Any = None) -> Image:
    image = Image.new("RGB", dimensions, (0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.rectangle([(0, 0), (128, 128)], fill=model)
    return image
