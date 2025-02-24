Maximum and Minimum of Numbers

numbers = []

while True:
    user_input = input("Enter a number (or 'done' to finish): ")
    if user_input.lower() == 'done':
        break
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a number.")

if numbers:
    print(f"Maximum: {max(numbers)}, Minimum: {min(numbers)}")
else:
    print("No numbers were entered.")
