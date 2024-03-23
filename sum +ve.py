#Given a list of numbers, create a function to find the sum of all positive numbers

def sum_of_positive_numbers(numbers):
    return sum(num for num in numbers if num > 0)

# Example usage:
number_list = [-1, 2, 5, -3, 10, -7]
positive_sum = sum_of_positive_numbers(number_list)
print("Sum of positive numbers:", positive_sum)
