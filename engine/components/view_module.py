from dataclasses import dataclass

from components import ControllerBase, ViewBase

@dataclass
class ViewModule:
  controller: ControllerBase
  view: ViewBase
  config: any