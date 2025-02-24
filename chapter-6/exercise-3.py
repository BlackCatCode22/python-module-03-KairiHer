def count(string, letter):
    count = 0
    for char in string:
        if char == letter:
            count += 1
    return count

# Example usage:
text = input("Enter a string: ")
char_to_count = input("Enter a letter to count: ")

result = count(text, char_to_count)
print(f"The letter '{char_to_count}' appears {result} times in the string.")
