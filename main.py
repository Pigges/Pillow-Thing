# Import
import random
from PIL import Image
import math

# TODO: fix "Invalid awnser!" bug for the filters that asks for value

img = False

# Credits
credits = """\nInformation:
By: Pigges
Version: 1.0
This is a simple image manipulation tool made in school
"""

# Ask for the option text
def menu_ask(loaded):
    return f"""\nMenu
Loaded: {loaded}
----------
[1] Filter
[2] Load file (filename)
[3] Save file (filename)
[4] Information
[5] Exit
----------
Choose option: """

# Ask for the filter text
def filter_ask(loaded): return """\nFilters
----------
[1]: Gray scale
[2]: Color shift
[3]: Invert color
[4]: Brigher (1-10)
[5]: Darker (1-10)
[6]: Noise (1-3)
----------
Choose filter: """

# Ask for a value
def value_ask(limit):
    return f"\nValue [1-{limit}]: "    

# Make the image grayscale
def grayScale():
    for y in range(img.height): # Go through the image verticaly to get y
        for x in range(img.width): # Go through the image horizontaly to get x
            pixel = img.getpixel((x, y)) # Fetch the pixel
            mean_value = math.floor((pixel[0] + pixel[1] + pixel[2])/3) # Get the mean value of the color values
            pixel = (mean_value, mean_value, mean_value) # Reassing the pixel variable with the new gray scaled values
            img.putpixel((x, y), pixel) # Put the pixel value in the current position

# Color shift the image
def colorShift():
    for y in range(img.height): # Go through the image verticaly to get y
        for x in range(img.width): # Go through the image horizontaly to get x
            pixel = img.getpixel((x, y)) # Fetch the pixel
            pixel = (pixel[1], pixel[2], pixel[0]) # Shift the color values
            img.putpixel((x, y), pixel) # Put the pixel value in the current position

# Invert the image
def invertColor():
    for y in range(img.height): # Go through the image verticaly to get y
        for x in range(img.width): # Go through the image horizontaly to get x
            pixel = img.getpixel((x, y)) # Fetch the pixel
            pixel = (255 - pixel[0], 255 - pixel[1], 255 - pixel[2]) # Invert color by doing: 255 - value
            img.putpixel((x, y), pixel) # Put the pixel value in the current position

# Brighten the image
def brighter():
    # Ask user for a number between 1-10
    value = ((menu(range(1, 11), value_ask(10))+1)/10)+1

    for y in range(img.height): # Go through the image verticaly to get y
        for x in range(img.width): # Go through the image horizontaly to get x
            pixel = img.getpixel((x, y)) # Fetch the pixel
            pixel = (math.floor(pixel[0]*value), math.floor(pixel[1]*value), math.floor(pixel[2]*value)) # Multiplying all color values with the value factor
            img.putpixel((x, y), pixel) # Put the pixel value in the current position

# Darken the image
def darker():
    # Ask user for a number between 1-10
    value = ((menu(range(1, 11), value_ask(10))+1)/10)+1

    for y in range(img.height): # Go through the image verticaly to get y
        for x in range(img.width): # Go through the image horizontaly to get x
            pixel = img.getpixel((x, y)) # Fetch the pixel
            pixel = (math.floor(pixel[0]/value), math.floor(pixel[1]/value), math.floor(pixel[2]/value)) # Dividing all color values with the value denominator
            img.putpixel((x, y), pixel) # Put the pixel value in the current position

# Create noise in the image
def noise():
    # Ask user for a number between 1-3
    value = menu(range(1, 4), value_ask(3))+1
    if (value == 1): value = 10 # %
    elif (value == 2): value = 40 # %
    elif (value == 3): value = 80 # %

    for y in range(img.height): # Go through the image verticaly to get y
        for x in range(img.width): # Go through the image horizontaly to get x
            if (random.randint(0, 100) < value):
                pixel = img.getpixel((x, y)) # Fetch the pixel
                pixel = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                img.putpixel((x, y), pixel) # Put the pixel value in the current position

# Load a file
def loadFile():
    while True:
        # Try to load file; except if it does not exist
        try:
            img = Image.open(input("Enter file name: ./"))
            break
        except:
            print("File not found..")
    # Return the loaded file
    return ["img", img]

def saveFile():
     # Make sure that a file is loaded
    if (not img): 
        input("No file loaded.\nPress Enter to continue... ")
        return
    while True:
        try:
            filename = input("Save file as: ./")
            img.save(filename)
            input(f"File saved as: {filename}\nPress Enter to continue: ")
            break
        except:
            print("Error saving file..")
    return


# Function to show information about this program
def information():
    print(credits)
    input('Press ENTER to continue... ')

# Exit program
def exit():
    print('\nExiting!')
    return ['exit']

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
    loadFile,
    saveFile,
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
    noise
]

# The menu function
def menu(list, ask): # Get the appropriate list and question
    # Loop asking for the filter till awnser is valid
    while True:
        # Try converting awnser to integer
        try:
            loaded = img.filename if img else "None"
            response = int(input(ask(loaded))) # Ask the user what filter they want to use
            if (response >= 0 and response <= len(list)): # Make sure the awnser is within the correct range. If so, break 
                break
            else: print("\nOut of range!") # Tell the user that the number was out of range
        except:
            # Tell the user that the awnser was invalid
            print("\nInvalid awnser!")
    return response-1 # Return the awsner minus one because lists start at 0


while True:
    response = menu_list[menu(menu_list, menu_ask)]()
    if response:
        if (response[0] == 'img'):
            img = response[1]
        elif (response[0] == 'exit'):
            break