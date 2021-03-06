import board
import neopixel
from time import sleep

# Welcome Message
print("Hello, Light Master!")

# Output user's config info
print("\nBeginning test light operation with perams: ")
print('Pixels: 10')
print('Brightness: 1')
print('Color: (255, 0, 0)')

# Assign the pixels to be modified and give the new brightness
pixels = neopixel.NeoPixel(
    board.D18, 1000, brightness=1, auto_write=False, pixel_order=neopixel.GRB)

# Clear any Existing color data
pixels.fill((0, 0, 0))
print("Cleared existing pixel info.")
sleep(2)
# Assign the new colors
pixels.fill((255, 0, 0))
pixels.show()
print('Updated pixel color info to: (255, 0, 0).')

# Notify user of script completion
print("\nFinished sending pixel instructions.")
