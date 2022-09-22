from dataclasses import dataclass

from .controller import ControllerBase
from .view import ViewBase

@dataclass
class ViewModule:
  controller: ControllerBase
  view: ViewBase
  config: any