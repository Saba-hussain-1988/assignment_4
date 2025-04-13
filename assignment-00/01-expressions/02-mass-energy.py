"""
Problem Statement
Write a program that continually reads in mass from the user and then outputs the equivalent energy using 
Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:

E = m * c**2
the speed of light -- C = 299792458 m/s.
"""
C = 299792458 # m/s

def main():
    # take input for mass in kilograms and convert into float type
    mass = float(input("Enter the mass value in kilograms: ")) # in kg
    print("\n")
    # calculate the energy by using the mass-energy equivalence formula
    print("Mass-Energy Equivalence formula is: \033[92m e = m * (C^2)\033[0m", "\n")
    energy = mass * (C**2)

    print(f"m = Mass in kilograms = \033[1;3m{mass}kg\033[0m", "\n")

    print(f"C = speed of light = \033[1;3m{C}m/s\033[0m", "\n")

    print(f"Energy is = \033[1;3m{energy}joules\033[0m")

if __name__ == "__main__":
    main()




