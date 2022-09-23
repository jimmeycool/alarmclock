from PIL import ImageFont
from PIL.ImageFont import FreeTypeFont

##COLORS
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
BLACK = (0, 0, 0, 0)

def get_verdana_font(size: int) -> FreeTypeFont: 
    return ImageFont.truetype('verdana.ttf', size)

def get_arial_font(size: int) -> FreeTypeFont:
    return ImageFont.truetype("arial.ttf", size)