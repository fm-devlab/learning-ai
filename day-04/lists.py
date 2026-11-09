# Create a list of five integers
numbers = [1, 2, 3, 4, 5]

# Print the first and the last element (-1 always points to the last one)
print(numbers[0], numbers[-1])

# Print how many elements the list has
print(len(numbers))

# Add a new element at the end of the list
numbers.append(6)

# The last element and the length have changed
print(numbers[0], numbers[-1])
print(len(numbers))

# Loop through the list and print every element
for number in numbers:
    print(number)