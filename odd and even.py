#Write a function to check if a number is even or odd and return "Even" or "Odd" accordingly

def even_odd_number(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
number = int(input("Enter a number: "))
results = even_odd_number
print(f"The number {number} is {results}")
