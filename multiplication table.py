#Create a function that takes a number as input and prints its multiplication table.

def multiplication_table(number):
    """
    Prints the multiplication table of a given number.

    Parameters:
        number (int): The number for which to print the multiplication table.
    """
    print("Multiplication table for", number)
    for i in range(1, 11):
        print(number, "x", i, "=", number * i)

# Example usage:
number = 7
multiplication_table(number)
