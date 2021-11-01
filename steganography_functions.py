import random
import urllib.request
from PIL import ImageDraw, Image
import string
import imghdr

def get_unshuffled_list(seeded_list, order_list):
    """
        Unshuffles a seeded list with a given order list (a list seeded using the same seed).
        Returns the unshuffled list.
    """
    unshuffled_list = [0]*len(seeded_list)   # empty list, but the right length
    for i,originalIndex in enumerate(order_list):
        unshuffled_list[originalIndex] = seeded_list[i]
    return unshuffled_list

def get_order_list(list_size, seed):
    """
        Creates a simple seeded list using a given seed and list size.
        Returns the order list.
    """
    order_list = list(list_size)
    random.seed(seed)
    random.shuffle(order_list)
    return order_list
    
def create_seeded_list(initial_list, seed):
    """
        Randomises a list using a given seed.
        Returns the seeded list.
    """
    seeded_list = initial_list.copy()
    random.seed(seed)
    random.shuffle(seeded_list)

    sample_pixel_list = []
    for i in range(10):
        sample_pixel_list.append(seeded_list[i])
    print('First ten pixels of the seeded list are printed below: '+str(sample_pixel_list)+"\n")
    return seeded_list
    
def randomise_list(initial_list):
    """
        Randomises the entered list.
        Returns the randomised list.
    """
    randomlist = initial_list.copy()
    random.shuffle(randomlist)
    return randomlist

def word_selection():
    """
        Loops until the user enters a valid list of strings.
        Returns the valid list of strings.
    """
    random_word_list = []
    invalidChars = set(string.punctuation.replace("_", ""))

    while len(random_word_list) < 6:
        user_input = input("Please enter word "+str(len(random_word_list)+1)+" with no punctuation: ")
        if not any(char in invalidChars for char in user_input) and len(user_input) > 0:
            random_word_list.append(user_input.replace(" ",""))
        else:
            print("Invalid Word!")
    return random_word_list

def seed_entry():
    """
        Loops until the user enters a valid seed string.
        Returns the valid seed string.
    """
    invalidChars = set(string.punctuation.replace("_", ""))

    while True:
        user_input = input("Enter a random word to be used as a seed: ")
        if not any(char in invalidChars for char in user_input) and len(user_input) > 0:
            print("")
            print("Seed chosen: "+user_input)
            return user_input
        else:
            print("Invalid Word!")

def download_and_convert_image():
    while True:
        try:
            user_image_url = input("Paste the whole url of an image on Imgur ('Copy image link')' or leave blank for an example image:")
            if not user_image_url:
                user_image_url = "https://i.imgur.com/h5bQ158.jpeg"
            urllib.request.urlretrieve(user_image_url, 'image.png')
            
            image = Image.open('image.png')
            image.save("converted.png", format="png")
            converted_image = Image.open('converted.png')
            print("Converted image to png regardless and saved as converted.png \n")
            if imghdr.what('converted.png') == 'png':
                return converted_image
        except Exception as e:
            print("Error using that image, please try another")

def add_seed_to_corner_of_image(image, seed):
    draw = ImageDraw.Draw(image)
    width, height = image.size
    text_width, text_height = draw.textsize(seed)

    while True:
        position_choice = input("Please choose which corner to put your text: 'tl' (top left), 'tr' (top right), 'bl' (bottom left), 'tr' (top right): \n")    
        if position_choice.lower() == 'tl':
            position = (0, 0)
            break
        elif position_choice.lower() == 'tr':
            position = (width - text_width, 0)
            break
        elif position_choice.lower() == 'bl':
            position = (0, height - text_height)
            break
        elif position_choice.lower() == 'br':
            position = (width - text_width, height - text_height)
            break
        elif not position_choice:
            position = (width - text_width, height - text_height)
            break
        else:
            print("Invalid entry, please enter one of: 'tl', 'tr', 'bl, 'tr' \n")

    while True:
        colour_choice = input("Please choose which colour for you text: 'white', 'black': \n")    
        if colour_choice.lower() == 'white':
            colour = (255,255,255)
            break
        elif colour_choice.lower() == 'black':
            colour = (0,0,0)
            break
        else:
            print("Invalid entry, please enter one of: 'white', 'black' \n")
    draw.text(position, seed, colour)

    image.save("converted_image_with_seed_in_corner.png", format="png")
    return image

def convert_image_into_pixels(image):
    # Load the image into a PixelAccess class object called "pixel_map"
    pixel_map = image.load()

    # Make a tuple to store the x,y image size
    image_size = image.size

    # start yet another list, this one is called "list_of_pixels", I'm not sure why
    list_of_pixels = []

    # Finally we'll iterate over the "pixel_map" and add the RGB tuples to our "list_of_pixels"
    for y in range(image_size[1]):
        for x in range(image_size[0]):
            # Get the RGB values (as a string tuple) from the current pixel
            rgb = pixel_map[x,y]
            r, g, b = rgb
            # we don't need the alpha, so it's discarded
            list_of_pixels.append((r, g, b))

    sample_pixel_list = []
    for i in range(10):
        sample_pixel_list.append(list_of_pixels[i])
    print('First ten pixels of the image are printed below: '+str(sample_pixel_list)+"\n")
    return list_of_pixels

def create_image_from_list_of_pixels(list_of_pixels, image_size):
    image = Image.new("RGB", image_size)
    image.putdata(list_of_pixels)
    return image