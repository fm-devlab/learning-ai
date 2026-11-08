# Day 02

## What I did
- Learned how a program makes decisions with `if`, `elif` and `else`.
- Wrote three programs: decisions.py (age check), grades.py (Swiss grades) and cinema.py (ticket price).
- Used nested conditions and combined them with `and`.

## What I got wrong
- Swapped the two messages in decisions.py, so a 25-year-old was "too young".
- Used `<=` instead of `<`: the test with 18 showed that 18 ended up in the wrong branch.
- In grades.py my condition rejected the grade 1, which is valid.
- In cinema.py I got a NameError: `price` did not exist in the invalid-age branch, so the last print failed.
- `"Yes"` with a capital letter does not match `"yes"`, because Python is case sensitive.

## What I understood
- Edge cases (the values on the boundary) are the ones that reveal logic errors: always test one value per side.
- `>=` and `<` cover all cases without overlapping, while `>=` and `<=` overlap on the boundary.
- Python checks the branches from top to bottom and stops at the first true one, so the order matters.
- A variable exists only after it has been given a value, in every possible branch.
- The `else` branch catches everything not caught before, including invalid values.