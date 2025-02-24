text = input("Enter a string: ")
index = len(text) - 1  # Start at the last character

while index >= 0:
    print(text[index])  # Print the character at the current index
    index -= 1  # Move to the previous character
