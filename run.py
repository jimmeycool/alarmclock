import time
from config import device_configs, screen_configs
from alarmclock import load

def main():
  render_modules = load(device_configs, screen_configs)

  while True:
    _ = [mod.execute() for mod in render_modules]
    time.sleep(0.01)


if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    pass
