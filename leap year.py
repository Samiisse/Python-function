#Implement a function to check if a given year is a leap year or not"

def is_leap_year(year):
    """
    Check if a given year is a leap year or not.

    Parameters:
        year (int): The year to check.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True  # Year divisible by 400 is a leap year
            else:
                return False  # Year divisible by 100 but not 400 is not a leap year
        else:
            return True  # Year divisible by 4 but not 100 is a leap year
    else:
        return False  # Year not divisible by 4 is not a leap year

# Example usage:
year = 2024
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
