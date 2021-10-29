import random
import urllib.request
from PIL import ImageDraw, Image
import string
from steganography_functions import *
import imghdr
def exercise_two():
    """
    
    """
    print("In this exercise, we will retrieve an image from Imgur, some text from pastebin and send a secret message within our image.\n")
    converted_image = download_and_convert_image()
    # input("Press any key to start the process of adding a seed to the image's corner...\n")
    seed = seed_entry()
    converted_image_with_text = add_seed_to_corner_of_image(converted_image, seed)    
    list_of_pixels = convert_image_into_pixels(converted_image_with_text)
    seeded_list_of_pixels = create_seeded_list(list_of_pixels, seed)
    scrambled_image = create_image_from_list_of_pixels(seeded_list_of_pixels, converted_image_with_text.size)
    scrambled_image.save("scrambled_image.png", format="png")

    # For sake of demo only, we will get the pixels of the scrambled image.
    new_seeded_list_of_pixels = convert_image_into_pixels(scrambled_image)

    order_list = get_order_list(range(len(new_seeded_list_of_pixels)), seed)
    unscrambled_list_of_pixels = get_unshuffled_list(new_seeded_list_of_pixels, order_list)
    unscrambled_image = create_image_from_list_of_pixels(unscrambled_list_of_pixels, converted_image_with_text.size)
    unscrambled_image.save("unscrambled_image.png", format="png")
    pass