import random
from steganography_functions import *

def exercise_one():
    """
        First lets build a simple ordered list. We'll use the random function to decide the length, then make a simple linear list.
        We'll make the simply list a bit spicy by adding some words to each entry.
    """
    input("Press any key to start... You will be asked to choose 6 random words. \n")

    random_word_list = []
    invalidChars = set(string.punctuation.replace("_", ""))

    random_word_list = word_selection()
    
    print("You have chosen: " + str(random_word_list)+" \n")
    input("Press any key to start Exercise One... \n")

    dice = random.randint(100,300)
    initial_list = []

    input("Press any key to generate an initial list... \n")

    for i in range(dice):
        initial_list.append(str(i)+'-'+random.choice(random_word_list))
        
    print(str(initial_list) + "\n")
    print('Initial List length: ' + str(dice)+ " \n")
    input("Now we have a pretty, linear list. Press any key to randomise it... \n")
    randomlist = randomise_list(initial_list)
    print(str(randomlist)+" \n")
    input("Let's randomise the initial list again. Press any key to randomise it... \n")
    randomlist = randomise_list(initial_list)
    print(str(randomlist)+" \n")
    print("Problem is, with this randomised list, there is no way to return the list to it's original format. That's where a seed comes in, a lot like what you use in Minecraft to generate the world. \n")
    seed = seed_entry()
    input("Press any key to randomise our initial list using '"+seed+"' as a seed... \n")
    seeded_list = create_seeded_list(initial_list, seed)
    print(str(seeded_list)+" \n")
    input("Press any key to randomise our initial list using '"+seed+"' as a seed again... \n")
    seeded_list = create_seeded_list(initial_list, seed)
    print(str(seeded_list)+" \n")
    print("Notice how the list is the same each time is it pseudorandomised with the seed. \n")
    input("Press any key to start the process of unshuffling the list using our seed '"+seed+"'... \n")
    order_list = get_order_list(range(len(seeded_list)), seed)
    print(str(order_list)+" \n")
    print("Simple list shuffled using the seed '"+seed+"'. The numbers match the pseudorandomised list we created earlier. We will call this the order list.\n")
    print("Now we have a order list, shuffled into the same position as our pseduorandomsed list. Now all we need to do is use the order list to unshuffle our seeded list. \n")
    input("Press any key to unshuffle the seeded list using our order list... \n")
    print(str(get_unshuffled_list(seeded_list, order_list))+" \n")
