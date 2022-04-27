
# Import
from PIL import Image
import random

# Load an image
img = Image.open('foto_coolt.jpg')

# Fetch the color value of a specific pixel
pixel = img.getpixel((0, 0)) # Type: tuple (x, y)

# Create a color
# r, g, b = Red, Green, Blue
color = (0, 10, 200) # Type: tuple (r, g, b)

# Paint a pixel with a color
img.putpixel((0, 0), color) # First element is position (x, y). Second element is the color (r, g, b)

# Nested loop to go through every pixel
for y in range(img.height):
    for x in range(img.width):

        # Get the pixel value
        pixel = img.getpixel((x, y)) # Type tuple: (x, y). Response list [r, g, b]
        red = pixel[0]
        green = pixel[1]
        blue = pixel[2]

        # Change the color values
        red += random.randint(0, 255-red)
        green += random.randint(0, 255-green)
        blue += random.randint(0, 255-blue)

        pixel = (red, green, blue) # Give pixel the new color values

        # Change the current pixel
        img.putpixel((x, y), pixel)


# Show the image
#img.show()

# Save the image
img.save('foto_coolt.png')