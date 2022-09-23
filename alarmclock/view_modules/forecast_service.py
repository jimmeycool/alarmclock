from asyncio import create_task
import json
import aiohttp

forecast_task = None

async def fetch_forecast():
  async with aiohttp.ClientSession() as session:
    async with session.get("https://api.weather.gov/points/47.6035,-122.3294") as location_reponse:
      location = json.loads(await location_reponse.text())
      async with session.get(location["properties"]['forecastHourly']) as forecast_response:
        forecast = json.loads(await forecast_response.text())
        return forecast["properties"]["periods"]


async def get_forecast():
  global forecast_task
  if forecast_task == None:
    forecast_task = create_task(fetch_forecast())

  return await forecast_task