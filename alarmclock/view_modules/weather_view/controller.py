from dataclasses import dataclass
import aiohttp
from io import BytesIO
from typing import Any
from PIL import Image
import json

from alarmclock.engine.components import AsyncControllerBase
from alarmclock.view_modules.forecast_service import get_forecast


@dataclass
class WeatherModel:
  image: Image
  desc: str
  time: str
  temp: int

class Controller(AsyncControllerBase):

  def __init__(self, config: Any = None) -> None:
    super().__init__(config)
    self.images = {}
    self.model = None
    self.periods = None
    self.current_period = 0

  async def fetch(self) -> None:
    if self.periods == None:
      self.periods = await get_forecast()

    period = self.periods[self.current_period]
    async with aiohttp.ClientSession() as session:
      async with session.get(period['icon']) as response:
        b = await response.read()
        bytes = BytesIO(b)
        im = Image.open(bytes)
        self.model = WeatherModel(
          im,
          period["shortForecast"],
          period["startTime"],
          period["temperature"],
        )
        self.current_period += 1
