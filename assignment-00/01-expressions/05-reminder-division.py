"""
Problem Statement
Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

(user input is in bold italics):
"""

def main():
    # take inputs from user
    dividend = int ( input ("Enter a integer to be divided: "))
    divisor = int ( input ("Enter a integer divided by: "))

    # calculation
    quotient = dividend // divisor
    remainder = dividend % divisor

    print(f"The result of this division is \033[92m{quotient}\033[0m with a remainder of \033[92m{remainder}\033[0m .")


if __name__ == "__main__":
    main()