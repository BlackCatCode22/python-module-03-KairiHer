strip() Example:
text = "  Hello World!  "
stripped_text = text.strip()

print(f"'{stripped_text}'")  # Output: 'Hello World!'

replace() Example:
sentence = "I like Python. Python is great!"
replaced_sentence = sentence.replace("Python", "Java")

print(replaced_sentence)  # Output: 'I like Java. Java is great!'

find() Example:
text = "apple, banana, cherry"
position = text.find("banana")

print(position)  # Output: 7 (index where "banana" starts)

upper() and lower() Example:
text = "Hello World"
print(text.upper())  # Output: 'HELLO WORLD'
print(text.lower())  # Output: 'hello world'

split() Example:
sentence = "apple,banana,cherry"
fruits = sentence.split(",")

print(fruits)  # Output: ['apple', 'banana', 'cherry']
