# Create a dictionary: each key has a value
person = {"name": "Jack", "age": 25, "city": "London"}

# Read a value using its key
print(person["name"])

# Change the value of an existing key
person["age"] = 20
print(person["age"])

# Add a new key by assigning a value to it
person["job"] = "plumber"

# Print the whole dictionary
print(person)

# Loop over the keys and print each key with its value
for key in person:
    print(key, person[key])

# get() returns a fallback value when the key does not exist (no KeyError)
print(person.get("salary", "not available"))