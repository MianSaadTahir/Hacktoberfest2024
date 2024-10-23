# Slightly Complex Python Program: Check if a string is a palindrome

def is_palindrome(s):
    # Remove spaces and convert the string to lowercase for accurate comparison
    cleaned_string = s.replace(" ", "").lower()
    
    # Check if the cleaned string is the same when reversed
    return cleaned_string == cleaned_string[::-1]

# Input from the user
user_input = input("Enter a string to check if it's a palindrome: ")

# Output result
if is_palindrome(user_input):
    print(f"'{user_input}' is a palindrome!")
else:
    print(f"'{user_input}' is not a palindrome.")
