# Ask for the age and convert the answer to an integer
age = int(input("What's your age? "))

# Check the boundary case: 18 is an adult, so only values below 18 are too young
if age < 18:
    # Runs only when the condition above is true
    print("Too young")
else:
    # Runs in every other case (18 or more)
    print("Access granted")