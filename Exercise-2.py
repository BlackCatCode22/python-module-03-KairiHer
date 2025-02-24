numbers = []

while True:
    user_input = input("Enter a number: ")
    if user_input.lower() == 'done':
        break
    try:
        number = int(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter an integer.")

if numbers:
    print(f"Maximum: {max(numbers)}, Minimum: {min(numbers)}")
else:
    print("No valid numbers were entered.")
