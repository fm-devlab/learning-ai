# Day 01

## What I did
- Set up Git by hand: init, add, commit, diff, log, push, clone, pull.
- Published two repos on GitHub and built my profile README.
- Wrote my first Python programs: hello.py, types.py and age.py.

## What I got wrong
- Wrote `name = input` without parentheses, so `name` became the function itself and not the answer.
- Thought `age + 5` would work after `input()`. It failed because `input()` always returns a string.
- Thought `int("25.5")` would cut the decimals. It raises a ValueError: only `int(25.5)` does that.
- Mixed up `//` (integer division) and `%` (remainder).
- My push was rejected because GitHub had a commit I did not have locally.

## What I understood
- A variable is a name that points to a value, created with `name = value`.
- `input()` always returns a string, so I convert it with `int()` or `float()`.
- The type decides the behavior: `+` joins strings but adds numbers.
- Run `git pull` before working, so my computer and GitHub start from the same point.
- Error messages say where to look: the line number and the error type.