# Pillow
from PIL import ImageGrab
import time
time.sleep(10)
i = 0
while i < 9:
  time.sleep(1)
  i += 1
  img = ImageGrab.grab()
  img.save(f"capture{i}.png")
