"""
Problem Statement
Converts feet to inches. Feet is an American unit of measurement.
There are 12 inches per foot. Foot is the singular, and feet is the plural.
"""

def main():
    print("\033[92mThe program converts the length unit from feet to inches.\033[0m")
    # as we know,
    # 1 foot = 12 inches

    # take input from user in feet and convert into float type
    feet_input = float ( input("enter the length in feet: "))

    convert_into_inches = feet_input * 12

    print(f"The \033[1;3m{feet_input}\033[0m feet are equals to \033[1;3m{convert_into_inches}\033[0m inches.")

if __name__ == "__main__":
    main()