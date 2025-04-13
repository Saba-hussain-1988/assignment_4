"""
Problem Statement
Write a program to solve this age-related riddle!

Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

Anton is 21 years old.

Beth is 6 years older than Anton.

Chen is 20 years older than Beth.

Drew is as old as Chen's age plus Anton's age.

Ethan is the same age as Chen.

Your code should store each person's age to a variable and print their names and ages at the end.
The autograder is sensitive to capitalization and punctuation, be careful! Your solution should look like this (the below numbers are made up -- your solution should have the correct values!):
"""

def main():
    print("\033[92mAge-related Riddle\033[0m")
    anton = 21  # his given age
    beth = anton + 6 # Beth is 6 years older than Anton.
    chen = beth + 20 # Chen is 20 years older than Beth.
    drew = chen + anton # Drew is as old as Chen's age plus Anton's age.
    ethan = chen # Ethan is the same age as Chen.

    print(f"Anton age is: \033[92;3m{anton}\033[0m.")    
    print(f"Beth age is: \033[92;3m{beth}\033[0m.")
    print(f"Chen age is: \033[92;3m{chen}\033[0m.")
    print(f"Drew age is: \033[92;3m{drew}\033[0m.")
    print(f"Ethan age is: \033[92;3m{ethan}\033[0m.")    
    

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()