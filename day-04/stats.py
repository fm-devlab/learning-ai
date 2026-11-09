# List of numbers to analyze
numbers = [4, 8, 15, 16, 23, 42]

# Sum: start from 0 and add every number inside the loop
total = 0
for number in numbers:
    total += number
print(total)

# Average: the sum divided by how many elements the list has (always a float)
print(total / len(numbers))

# Smallest and largest value, using built-in functions
print(min(numbers))
print(max(numbers))