# Import
import random
import sys
from tqdm import tqdm
from PIL import Image
import math

# TODO: fix "Invalid answer!" bug for the filters that asks for value

img_org = False
img = False

# Credits
credits = """\nInformation:
By: Pigges
Version: 1.0
This is a simple image manipulation tool made in school
"""

# Ask for the option text
menu_ask = f"""\nMenu
----------
[1] Filter
[2] Load image (filename)
[3] Save image (filename)
[4] Revert changes
[5] Information
[6] Exit
----------"""

# Ask for the filter text
filter_ask = """\nFilters
----------
[1]: Gray scale
[2]: Color shift
[3]: Invert color
[4]: Brighter (1-10)
[5]: Darker (1-10)
[6]: Noise (1-3)
[7]: Pixelate (1-10)
[8]: Blur (1-10)
----------
Choose filter: """

# Ask for a value
def value_ask(range):
    while True:
        try:
            answer = int(input(f"Choose a number [1-{range}]: "))
        except KeyboardInterrupt:
            print("\nExiting menu!")
            break
        except:
            print("Invalid number!")
        if (not answer < 1 and not answer > range):
            return answer
        else:
            print("Value out of range!")

# Make the image grayscale
def grayScale():
    global img
    for y in range(img.height): # Go through the image vertically to get y
        for x in range(img.width): # Go through the image horizontally to get x
            pixel = img.getpixel((x, y)) # Fetch the pixel
            mean_value = math.floor((pixel[0] + pixel[1] + pixel[2])/3) # Get the mean value of the color values
            pixel = (mean_value, mean_value, mean_value) # Resizing the pixel variable with the new gray scaled values
            img.putpixel((x, y), pixel) # Put the pixel value in the current position

# Color shift the image
def colorShift():
    global img
    for y in range(img.height): # Go through the image vertically to get y
        for x in range(img.width): # Go through the image horizontally to get x
            pixel = img.getpixel((x, y)) # Fetch the pixel
            pixel = (pixel[1], pixel[2], pixel[0]) # Shift the color values
            img.putpixel((x, y), pixel) # Put the pixel value in the current position

# Invert the image
def invertColor():
    global img
    for y in range(img.height): # Go through the image vertically to get y
        for x in range(img.width): # Go through the image horizontally to get x
            pixel = img.getpixel((x, y)) # Fetch the pixel
            pixel = (255 - pixel[0], 255 - pixel[1], 255 - pixel[2]) # Invert color by doing: 255 - value
            img.putpixel((x, y), pixel) # Put the pixel value in the current position

# Brighten the image
def brighter():
    global img
    # Ask user for a number between 1-10
    value = value_ask(10)

    for y in range(img.height): # Go through the image vertically to get y
        for x in range(img.width): # Go through the image horizontally to get x
            pixel = img.getpixel((x, y)) # Fetch the pixel
            pixel = (math.floor(pixel[0]*value), math.floor(pixel[1]*value), math.floor(pixel[2]*value)) # Multiplying all color values with the value factor
            img.putpixel((x, y), pixel) # Put the pixel value in the current position

# Darken the image
def darker():
    global img
    # Ask user for a number between 1-10
    value = value_ask(10)

    for y in range(img.height): # Go through the image vertically to get y
        for x in range(img.width): # Go through the image horizontally to get x
            pixel = img.getpixel((x, y)) # Fetch the pixel
            pixel = (math.floor(pixel[0]/value), math.floor(pixel[1]/value), math.floor(pixel[2]/value)) # Dividing all color values with the value denominator
            img.putpixel((x, y), pixel) # Put the pixel value in the current position

# Create noise in the image
def noise():
    global img
    # Ask user for a number between 1-3
    value = value_ask(3)
    if (value == 1): value = 10 # %
    elif (value == 2): value = 40 # %
    elif (value == 3): value = 80 # %

    for y in range(img.height): # Go through the image vertically to get y
        for x in range(img.width): # Go through the image horizontally to get x
            if (random.randint(0, 100) < value):
                pixel = img.getpixel((x, y)) # Fetch the pixel
                pixel = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                img.putpixel((x, y), pixel) # Put the pixel value in the current position
            
# Pixelate the image
def pixelate():
    global img
    # Ask user for a number between 1-10
    value = value_ask(10)

    _filename = img.filename # Save filename since menu() needs it later
    orgSize = img.size # Remember file size to scale up later
    img = img.resize( # Scaling down the image
        size=(orgSize[0] // value, orgSize[1] // value),
        resample=0)
    # Scaling it up to get pixelate effect
    img = img.resize(orgSize, resample=0)
    img.filename = _filename

# Blur the image with gaussian blur
def blur():
    global img
    _size = img.height * img.width
    valueDict = {
        1: 5,
        2: 7,
        3: 9,
        4: 11,
        5: 13,
        6: 15,
        7: 17,
        8: 19,
        9: 21,
        10: 23
    }
    # Ask user for a number between 1-10
    value = value_ask(10)
    _x = 0

    with tqdm(total=_size, desc="Gaussian Blurring", unit="Pixels", ncols=100) as pbar:
        for y in range(img.height): # Go through the image vertically to get y
            for x in range(img.width): # Go through the image horizontally to get x
                surroundingPixels = [] # Create a list of the surrounding pixels
                for i in range(valueDict[value]):  # Iterate through the surrounding pixels
                    for j in range(valueDict[value]):
                        try:
                            _pixel = img.getpixel((i+x, j+x)) # Get the pixel at the current position
                            surroundingPixels.append(_pixel) # Append the pixel to the surroundingPixels
                        except IndexError: # Ignore index error
                            pass
                r = sum(pixel[0] for pixel in surroundingPixels) / len(surroundingPixels)  # get the average red
                g = sum(pixel[1] for pixel in surroundingPixels) / len(surroundingPixels)  # get the average green
                b = sum(pixel[2] for pixel in surroundingPixels) / len(surroundingPixels)  # get the average blue
                img.putpixel((i, j),
                                (int(r), int(g), int(b)))  # set the pixel to the average of the surrounding pixels
                pbar.update(1)



# Load an image
def loadImg():
    global img
    global img_org
    while True:
        # Try to load image; except if it does not exist
        try:
            img_org = input("Enter image file name: ./")
            img = Image.open(img_org)
            break
        except KeyboardInterrupt:
            print("\nExiting menu!")
            break
        except:
            print("Image not found..")

def saveImg():
     # Make sure that an image is loaded
    if (not img): 
        input("No file loaded.\nPress Enter to continue... ")
        return
    while True:
        try:
            filename = input("Save file as: ./")
            img.save(filename)
            input(f"File saved as: {filename}\nPress Enter to continue: ")
            break
        except KeyboardInterrupt:
            print("\nExiting menu!")
            break
        except:
            print("Error saving file..")
    return

# Revert changes to image
def revert():
    global img
    while True:
        try:
            verify = input("Are you sure you want to revert changes? [y/N]: ")
            if (verify.lower() == 'y'):
                img = Image.open(img_org)
                print("Reverted SUCCESSFULLY!")
            elif (not verify):
                print("Revert CANCELED!")
            else:
                print("Unknown Answer!")
                continue
            input("Press Enter to continue: ")
            break
        except KeyboardInterrupt:
            print("\nExiting menu!")
            break
        except:
            print("Error reverting file!")


# Function to show information about this program
def information():
    print(credits)
    input('Press ENTER to continue... ')

# Exit program
def exit():
    print('\nExiting!')
    sys.exit()

# Handle filters menu
def filters():
    # Make sure that a file is loaded
    if (not img): 
        input("No file loaded.\nPress Enter to continue... ")
        return
    filter_list[menu(filter_list, filter_ask)]()
    input("Filter applied!\nPress Enter to continue... ")

# A list for the menu where each element points to the corresponding function
menu_list = [
    filters,
    loadImg,
    saveImg,
    revert,
    information,
    exit
]

# A list for the filters where each element points to the corresponding function
filter_list = [
    grayScale,
    colorShift,
    invertColor,
    brighter,
    darker,
    noise,
    pixelate,
    blur
]

# The menu function
def menu(list, ask): # Get the appropriate list and question
    # Loop asking for the filter till answer is valid
    while True:
        # Try converting answer to integer
        loaded = img.filename if img else False
        print(f"Loaded: {loaded}")
        print(ask)
        try:
            response = int(input("Enter value: ")) # Ask the user what filter they want to use
            if (response >= 0 and response <= len(list)): # Make sure the answer is within the correct range. If so, break 
                break
            else: print("\nOut of range!") # Tell the user that the number was out of range
        except KeyboardInterrupt:
            print("\nExiting menu!")
            sys.exit()
        except:
            print(Exception)
            # Tell the user that the answer was invalid
            print("\nInvalid answer!")
    return response-1 # Return the answer minus one because lists start at 0


print("""
Welcome to this Image manipulation script
made by Pigges,
using the Pillow package\n""")

# Start with loading an image
loadImg()

while True:
    response = menu_list[menu(menu_list, menu_ask)]()