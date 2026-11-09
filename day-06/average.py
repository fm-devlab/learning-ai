# Return the average of a list of numbers
def average(numbers):
    # Sum all the numbers with a loop
    total = 0
    for number in numbers:
        total += number
    # The return is outside the loop: it runs once, after the sum is complete
    return total / len(numbers)

# Average of the list from day 04: the result is a float
print(average([4, 8, 15, 16, 23, 42]))