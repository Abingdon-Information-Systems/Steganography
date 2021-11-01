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
    print("Adding your chosen seed word to the corner of your image (see converted_image_with_seed_in_corner.png).") 
    converted_image_with_text = add_seed_to_corner_of_image(converted_image, seed)  
    input("Press any key to convert your image with text layered on top to pixels... \n") 
    print("Here are some pixels for the image with text layered on top.") 
    list_of_pixels = convert_image_into_pixels(converted_image_with_text)
    input("Press any key to seed your new pixel list... \n") 
    seeded_list_of_pixels = create_seeded_list(list_of_pixels, seed)
    input("Press any key to turn your seeded list of pixels into an image called scrambled_image.png... \n") 
    scrambled_image = create_image_from_list_of_pixels(seeded_list_of_pixels, converted_image_with_text.size)
    scrambled_image.save("scrambled_image.png", format="png")

    # For sake of demo only, we will get the pixels of the scrambled image.
    print("Here are some pixels for the scrambled image.")
    new_seeded_list_of_pixels = convert_image_into_pixels(scrambled_image)

    order_list = get_order_list(range(len(new_seeded_list_of_pixels)), seed)
    unscrambled_list_of_pixels = get_unshuffled_list(new_seeded_list_of_pixels, order_list)
    unscrambled_image = create_image_from_list_of_pixels(unscrambled_list_of_pixels, converted_image_with_text.size)
    unscrambled_image.save("unscrambled_image.png", format="png")
    pass