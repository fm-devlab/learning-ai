# List of people: each person is a dictionary with a name and an age
people = [{"name": "Jack", "age": 25},
          {"name": "Mike", "age": 30},
          {"name": "Lisa", "age": 28}]

# Variables that collect results while the loop runs
total_age = 0
oldest_age = 0
oldest_name = ""

for person in people:
    # Print the name and age of the current person
    print(person["name"], person["age"])
    # Keep the oldest person seen so far (name and age are updated together)
    if person["age"] > oldest_age:
        oldest_name = person["name"]
        oldest_age = person["age"]
    # Add the current age to the running total
    total_age += person["age"]

# Average age: the sum divided by the number of people (a float)
print(total_age / len(people))

# Name and age of the oldest person
print(oldest_name, oldest_age)