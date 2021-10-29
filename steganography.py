import string
from exercise_one import exercise_one
from exercise_two import exercise_two
from steganography_functions import *

def main():

    while True:
        choice = input("Please choose which exercise you want to start or 'q' to quit (enter a number: '1','2'): \n")    
        if choice == '1':
            exercise_one()
        elif choice == '2':
            exercise_two()
        elif choice.lower() == 'q':
            break
        choice = print("Exercise complete!: \n")  
    print("Shutting down...")

if __name__ == "__main__":
    main()