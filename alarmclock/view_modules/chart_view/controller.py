from typing import Any
from alarmclock.engine.components.async_controller import AsyncControllerBase
from alarmclock.view_modules.forecast_service import get_forecast

class Controller(AsyncControllerBase):

  def __init__(self, config: Any = None) -> None:
    super().__init__(config)
    self.periods = None

  async def fetch(self) -> None:
    if self.periods == None:
      self.periods = await get_forecast()

    self.model.data = [x['temperature'] for x in self.periods[0:24]]