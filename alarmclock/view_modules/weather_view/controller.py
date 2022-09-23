from dataclasses import dataclass
from pickletools import bytes4
from tkinter import W
import aiohttp
from io import BytesIO
from typing import Any
from PIL import Image
import os
import json

from alarmclock.engine.components import AsyncControllerBase


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
    # with open(os.path.join('alarmclock', 'view_modules', 'weather_view', 'data.json')) as file:
    #   data = json.load(file)
    #   self.periods = data["properties"]["periods"]
    #   self.current_period = 0

  async def fetch(self) -> None:
    if self.periods == None:
      async with aiohttp.ClientSession() as session:
        async with session.get("https://api.weather.gov/points/47.6035,-122.3294") as location_reponse:
          location = json.loads(await location_reponse.text())
          async with session.get(location["properties"]['forecastHourly']) as forecast_response:
            forecast = json.loads(await forecast_response.text())
            self.periods = forecast["properties"]["periods"]

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
