import time
from config import device_configs, screen_configs
from alarmclock import start

if __name__ == "__main__":
  try:
    start(device_configs, screen_configs)
  except KeyboardInterrupt:
    pass
