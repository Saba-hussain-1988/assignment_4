"""
Problem Statement
Simulate rolling two dice, and prints results of each roll as well as the total.
"""

import random

def main():
    print ("\033[92;1mROLLING DICES\033[0m", "\n")
    # save the rang in a variable
    dice_range = 6

    # rolling dices
    dice1 = random.randint(1, dice_range)
    dice2 = random.randint(1, dice_range)

    total = dice1 + dice2

    print(f"\033[93mDice 1 have:\033[0m \033[1;3m{dice1}\033[0m")
    print(f"\033[93mDice 2 have:\033[0m \033[1;3m{dice2}\033[0m")
    print(f"\033[93mThe total of both dices is:\033[0m \033[1;3m{total}\033[0m")


if __name__ == "__main__":
    main()