from alarmclock.engine.components import ViewBase
from PIL import Image
from typing import Any, Tuple
import random
import math

class View(ViewBase):

  def __init__(self, config: Any = None) -> None:
    super().__init__(config)
    self.image = None
    self.pixels = None
    self.total_pixels = None
    self.filled_count = 0

  def scale_percent_progress(self, percent_progress: float):
    return percent_progress**2

  def color_pixel_by_index(self, pixel_position: int):
    y = pixel_position // self.dimensions[0]
    x = pixel_position % self.dimensions[1]
    self.image.putpixel((x, y), tuple(self.config["color"]))

  def draw(self, dimensions: Tuple[int, int], model: Any = None) -> Image:
    if self.image == None:
      self.dimensions = dimensions # todo, move to constructor
      self.image = Image.new("RGB", dimensions, (0, 0, 0))
      self.total_pixels = dimensions[0] * dimensions[1]
      self.pixel_sequence = list(range(0, self.total_pixels))
      random.shuffle(self.pixel_sequence)

    total_fill_percentage = self.scale_percent_progress(model.percent_progress)
    total_fill_count = math.ceil(total_fill_percentage * self.total_pixels)
    iteration_fill_count = total_fill_count - self.filled_count

    for _ in range(0, iteration_fill_count):
      pixel_position = self.pixel_sequence[self.filled_count]
      self.color_pixel_by_index(pixel_position)
      self.filled_count += 1

    return self.image.copy()
