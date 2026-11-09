# Day 05

## What I did
- Learned dictionaries: key-value pairs read by key instead of by position.
- Wrote dictionaries.py (read, change, add keys, loop, get) and people.py (a list of dictionaries).
- Calculated the average age and found the oldest person with a loop and an `if`.

## What I got wrong
- Used `person[1]` and `people["name"]` inside the loop: `person` is one dictionary at each round, while `people` is the whole list.
- Printed only the values in the loop, when I needed key and value together.
- Named a variable `totalAge`: in Python the convention is `total_age`.
- Found only the oldest age at first, not the name of the person.

## What I understood
- A dictionary is read by key (`person["name"]`), a list by position (`people[1]`).
- A missing key raises a KeyError, a missing position raises an IndexError.
- `get("key", fallback)` returns a fallback value instead of crashing.
- `people[1]["age"]` is read left to right: first the position in the list, then the key in the dictionary.
- Name and age of the oldest person must be updated together, inside the same `if`.
- With `>` the first of two equal maximums wins, with `>=` the last one.