"""
Problem Statement
Use Python to calculate the number of seconds in a year, and tell the user what the result is in a nice 
print statement that looks like this:

There are -- seconds in a year!

You should use constants for this exercise -- there are 365 days in a year, 
24 hours in a day, 60 minutes in an hour, and 60 seconds per minute.
"""

# constants
DAYS_PER_YEAR = 365
HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60
SECONDS_PER_MINUTE = 60


def main():
    # calculation
    hours_per_year = DAYS_PER_YEAR * HOURS_PER_DAY
    minutes_per_year = hours_per_year * MINUTES_PER_HOUR
    seconds_per_year = minutes_per_year * SECONDS_PER_MINUTE

    print(f"\033[93mThere are\033[0m \033[92;1m {seconds_per_year}\033[0m \033[93m seconds in a year.\033[0m")


if __name__ == "__main__":
    main()