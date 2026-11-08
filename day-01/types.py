# Create different variable types and printing the content + the type
name = "Jack"
print(name, type(name))
age = 25
print(age, type(age))
weight = 75.5 
print(weight, type(weight))

# Text value
name = "Jack"
print(name, type(name))

# Integer value
age = 25
print(age, type(age))

# Float value
weight = 75.5
print(weight, type(weight))

# Arithmetic with an integer
print(age + 5)

# Joining two strings
print(name + "Smith")

# Repeating a string
print(name * 3)

# Division always returns a float
print(age / 2)

# Integer division drops the decimals
print(age // 2)

# Remainder of the division
print(age % 2)

# Convert a number to a string before joining it to text
print(str(age) + " years old")

# This line raises a TypeError on purpose: str + int
print(name + age)