"""
Problem Statement
Write a program which asks the user what their favorite animal is,
and then always responds with "My favorite animal is also ___!"
(the blank should be filled in with the user-inputted animal, of course).

Here's a sample run of the program (user input is in bold italics -
note the space between the prompt and the user input!):
What's your favorite animal? cow
My favorite animal is also cow!
"""

# main function
def main():
    print(f"\033[92mThis program ask about user's favorite animal and always respond with\033[0m \033[1m\"My favorite animal is also ______\".\033[0m")
    user_input = input("What is your favorite animal?\t")
    print(f"My favorite animal is also \033[1;3m{user_input}\033[0m")
    

if __name__ == '__main__':
    main()


