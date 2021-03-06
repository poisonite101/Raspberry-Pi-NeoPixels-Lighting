import board
import neopixel
from time import sleep

# Welcome Message
print("Hello, Light Master!\n")

# Set Config Params
pixelCount = int(input("Enter number of pixels to modify: "))
brightness = float(input("Enter brightness of pixels (float between 0-1): "))

print("\nEnter the RGB data for color one(int between 0-255).")
red1 = int(input("Red: "))
green1 = int(input("Green: "))
blue1 = int(input("Blue: "))
print("\nEnter the RGB data for color two(int between 0-255).")
red2 = int(input("Red: "))
green2 = int(input("Green: "))
blue2 = int(input("Blue: "))

# Output user's config info
print("\nBeginning test light operation with perams: ")
print(f'Pixels: {pixelCount}')
print(f'Brightness: {brightness}')
print(f'\nColor One: ({red1}, {green1}, {blue1})')
print(f'Color Two: ({red2}, {green2}, {blue2})')

# Assign the pixels to be modified and give the new brightness
pixels = neopixel.NeoPixel(board.D18, pixelCount, brightness=brightness)

# Clear any Existing color data
pixels.fill((0, 0, 0))
print("Cleared existing pixel info.")
sleep(2)
# Assign the new colors
for i in range(pixelCount):
    if (i % 2) == 0:
        pixels[i] = (red1, green1, blue1)
    else:
        pixels[i] = (red2, green2, blue2)

pixels.show()
print(
    f'Updated pixel color info to:\n({red1}, {green1}, {blue1}) and ({red2}, {green2}, {blue2}).')

# Notify user of script completion
print("\nFinished sending pixel instructions.")
