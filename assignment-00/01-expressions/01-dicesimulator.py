"""
Problem Statement
Simulate rolling two dice, three times.
Prints the results of each die roll. This program is used to show how variable scope works.
"""

# Import the random library to generate random numbers
import random

def main():
    # using loop to rolling dices three times
    for i in range(3):
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        print(f"\033[92mRoll {i + 1}:\033[0m \n\tDice 1 = \033[1m{dice_1}\033[0m\n\tDice 2 = \033[1m{dice_2}\033[0m ")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()