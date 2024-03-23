#Write a Python function to check if a given string is a palindrome

def is_palindrome(s):
    # Convert the string to lowercase and remove non-alphanumeric characters
    s = ''.join(char.lower() for char in s if char.isalnum())
    # Compare the string with its reverse
    return s == s[::-1]

# Example usage:
test_string = "A man, a plan, a canal, Panama"
print("Is the string a palindrome?", is_palindrome(test_string))
