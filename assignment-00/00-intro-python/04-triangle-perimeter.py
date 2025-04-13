"""
Problem Statement
Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).

(user input is in bold italics):
"""

def main():
    # take inputs and convert string to float type
    print ("\033[92mThis program calculates the perimeter of triangle.\033[0m")
    side_1 = float(input("What is the length of side 1? "))
    side_2 = float(input("What is the length of side 2? "))
    side_3 = float(input("What is the length of side 3? "))

    # calculation of perimeter and covert into string type
    perimeter_of_triangle = str(side_1 + side_2 + side_3)

    print(f"The perimeter of the triangle is:  \033[1;3m{perimeter_of_triangle}\033[0m .")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()