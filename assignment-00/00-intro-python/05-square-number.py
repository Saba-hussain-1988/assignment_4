"""
Problem Statement
Ask the user for a number and print its square (the product of the number times itself).

Here's a sample run of the program (user input is in bold italics):

Type a number to see its square: 4

4.0 squared is 16.0
"""


def main():
    # take input and convert into float type
    num = float(input("Type a number to see its square: ")) 

    print(f"The square of \033[1;3m{num}\033[0m is: \033[92m{num ** 2}\033[0m") 


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
