"""
Problem Statement
Write a program which prompts the user for an adjective, then a noun, then a verb, 
and then prints a fun sentence with those words!

Mad Libs is a word game where players are prompted for one word at a time, 
and the words are eventually filled into the blanks of a word template to make an entertaining story! 
We've provided you with the beginning of a sentence (the SENTENCE_START constant) which will end in a 
user-inputted adjective, noun, and then verb.
"""

def story_making(noun, verb, adjective, location):
    story = (f"Yesterday, I saw {adjective} {noun} {verb} in a {location}.The {noun} was too {adjective} to {verb}. Everyone around was {verb}ing and having a {adjective} time.It was a really {adjective} day.")
    return story

def main():
    # take inputs from user
    adjective = input("Please enter an adjective: ")
    noun = input("Please enter a noun: ")
    verb = input("Please enter a verb: ")
    location = input("Please enter a suitable location: ")

    story = story_making(noun, verb, adjective, location)

    print(f"\033[92;1;3m STORY \033[0m \n\t \033[93m{story}\033[0m")

if __name__ == "__main__":
    main()