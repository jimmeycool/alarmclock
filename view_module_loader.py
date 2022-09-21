from dataclasses import dataclass
import importlib
from typing import Any
from engine.controller import ControllerBase
from engine.view import ViewBase

@dataclass
class ViewModule:
  controller: ControllerBase
  view: ViewBase
  config: any

def load(name: str, config: Any = None) -> ViewModule:
  """
  Dynamically loads a view module by name.

  Args:
      name (str): The name of the view module to load.
      config (Any, optional): Configuraion for the view module. Defaults to None.

  Returns:
      ViewModule: The dynamically loaded view module.
  """
  module = importlib.import_module(f"view_modules.{name}")
  return ViewModule(module.Controller(config), module.View(config), config)
