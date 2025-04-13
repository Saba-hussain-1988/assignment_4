"""
Problem Statement
Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.
The equation you should use for converting from Fahrenheit to Celsius is the following:

degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0

(Note. The .0 after the 5 and 9 matters in the line above!!!)

Here's a sample run of the program (user input is in bold italics):

Enter temperature in Fahrenheit: 76

Temperature: 76.0F = 24.444444444444443C
"""

def main():
    print("\033[92;3mThis program converts the unit of temperature from Fahrenheit to Celsius.\033[0m")
    # here I'm converting the input from string to float type
    input_value_in_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    # conversion calculation
    celsius_value = (input_value_in_fahrenheit - 32) * 5.0 / 9.0

    print(f"Temperature: \033[1;3m{input_value_in_fahrenheit}\033[0m\u2109 = \033[92m{celsius_value}\033[0m\u2103")

if __name__ == '__main__':
    main()