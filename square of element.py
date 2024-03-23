#Create a function to find the square of each element in a given list"

def square_elements(lst):
    return [x ** 2 for x in lst]

# Example usage:
given_list = [1, 2, 3, 4, 5]
squared_elements = square_elements(given_list)
print("Original list:", given_list)
print("Squared elements:", squared_elements)
