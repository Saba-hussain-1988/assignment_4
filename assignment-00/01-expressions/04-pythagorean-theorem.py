"""
Problem Statement
Write a program that asks the user for the lengths of the two perpendicular sides of a right 
triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!

For instance, let's consider a right triangle ABC, with the right angle located at C. According to the Pythagorean theorem:

AB ** 2 = BC ** 2 + AC ** 2
"""
import math

def main():
    print("\033[92mPythagorean Theorem\n")
    print("\033[93m(Hypotenuse)^2 = (perpendicular)^2 + (base)^2 \033[0m \n")
    # take inputs for base and perpendicular and convert into float type
    base = float( input("Enter the length of base: "))
    perpendicular = float (input("Enter the length of perpendicular: "))

    # calculation 
    hypotenuse = math.sqrt(perpendicular**2 + base**2)

    print(f"The length of Hypotenuse is: \033[1;3;94m{hypotenuse}\033[0m") 

if __name__ == "__main__":
    main()

