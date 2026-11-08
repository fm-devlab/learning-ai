# Ask if today is Tuesday (the answer is already a string)
tuesday = input("Is tuesday today? (yes/no) ")

# Ask for the age and convert the answer to an integer
age = int(input("What's your age? "))

# Tuesday discount: the price is 5 for everyone, so this check comes first
if tuesday == "yes":
    price = 5
else:
    # Child: from 1 to 11 years old
    if age < 12 and age > 0:
        price = 6
    # Adult: from 12 to 64 years old
    elif age > 11 and age < 65:
        price = 12
    # Senior: from 65 to 119 years old
    elif age < 120 and age > 0:
        price = 8
    # Anything else (0, negative numbers, 120 or more) is not a valid age
    else:
        print("Age not valid")
        # Give price a value anyway, otherwise the last print raises a NameError
        price = "n/a"

# Single print at the end: price always has a value by now
print("your price is " + str(price))