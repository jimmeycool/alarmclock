import time
from typing import Tuple, Any

from PIL import Image, ImageDraw

from alarmclock.engine.components import ViewBase
from alarmclock.view_modules.utilities import BLACK, get_arial_font, get_vardana_font


class View(ViewBase):

    def __init__(self, config: Any = None) -> None:
        super().__init__(config)

        # don't reload fonts on each render.
        self.ARIAL15 = get_arial_font(15)
        self.VARDANA30 = get_vardana_font(30)

    def draw(self, dimensions: Tuple[int, int], model: Any = None) -> Image:
        center = tuple(d//2 for d in dimensions)
        buttonRightCenter = tuple(c * 1.5 for c in center)
        topRightCenter = tuple((center[0] * 1.5, center[1] * 0.5))
        image = Image.new('RGB', dimensions, BLACK)
        draw = ImageDraw.Draw(image)
        hourMinute_str = time.strftime('%I:%M')
        second_str = time.strftime('%S')
        am_pm_str = time.strftime('%p')
        draw.text(center, text=hourMinute_str,
                  font=self.VARDANA30, anchor='mm')
        draw.text(buttonRightCenter, text=second_str,
                  font=self.ARIAL15, anchor='mm')
        draw.text(topRightCenter,
                  text=am_pm_str, font=self.ARIAL15, anchor='mm')
        return image
