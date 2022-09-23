from typing import Any

from alarmclock.engine.components import ControllerBase


class Controller(ControllerBase):
    def __init__(self, config: Any = None) -> None:
        super().__init__(config)
        self.position = (0, 0)

    def update(self) -> Any:
        return self.position
