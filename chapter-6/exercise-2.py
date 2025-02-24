In Python, the notation fruit[:] creates a slice of the string fruit, but without specifying any start or end indices. This means it returns a copy of the entire string.

Explanation of fruit[:]:
fruit[:] means "take all characters from the beginning to the end."
Since no start (: before) or end (: after) is specified, it defaults to taking everything.
The result is a new string that is identical to fruit, but it is a separate object in memory.

fruit = "banana"
copy_fruit = fruit[:]

print(copy_fruit)  # Output: banana
print(copy_fruit == fruit)  # Output: True (same content)
print(copy_fruit is fruit)  # Output: False (different objects in memory)
