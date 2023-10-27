from longest_palindrome import select_the_longest_palindrome

while True:
    user_input = input("Enter a string for search: ")
    print(f"The longest palindrome in user input is: {select_the_longest_palindrome(user_input)}")