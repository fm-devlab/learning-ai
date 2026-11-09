# Return the square of a number
def square(n):
    return n * n

print(square(5))

# Return True if the age is 18 or more, otherwise False
def is_adult(age):
    return age >= 18

# Test the values around the boundary: 17, 18 and 25
print(is_adult(17))
print(is_adult(18))
print(is_adult(25))

# This function only shows the result on screen: it returns nothing
def square_print(n):
    print(n * n)

# x receives None, because square_print has no return
x = square_print(5)
print(x)

# square(5) returns 25, so we can keep calculating with it
print(square(5) + 1)