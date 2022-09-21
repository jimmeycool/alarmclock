from view_module_loader import load
from PIL import Image, ImageDraw
from engine.mocks.pygame_display_adapter import PyGameDisplayAdapter
import time

def main():
  dimensions = (128, 128)
  display_adapter = PyGameDisplayAdapter(dimensions)
  
  # Specify the name of the view module you want to run here!
  view_module = load("hours_view")

  while True:
    # set up a new image for this tick
    image = Image.new("RGB", dimensions, (0, 0, 0))

    # Update controller and update image with the view
    model = view_module.controller.update()
    view_module.view.draw(ImageDraw.Draw(image), model)

    # Push update to display
    display_adapter.update(image)

    # Sleep  till next tick
    time.sleep(.01)

if __name__ == "__main__":
  main()
