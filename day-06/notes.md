# Day 06

## What I did
- Learned functions: `def`, parameters, `return` and how to call them.
- Wrote functions.py (square, is_adult, print vs return) and average.py (average of a list).
- Handled the edge case of an empty list.

## What I got wrong
- Wrote `(n * n) * n` in square: that is the cube, not the square.
- Tested only one value for is_adult, when the boundary values (17, 18, 25) are the ones that reveal errors.
- Thought a function with `print` does no calculation: it calculates, but the result does not come out of the function.
- Did not expect `average([])` to crash with a ZeroDivisionError: the list is empty, so `len(numbers)` is 0.

## What I understood
- `print` shows a value on screen, `return` hands it back to the caller so it can be stored and reused.
- A function without `return` gives back `None`, so `x = square_print(5)` makes `x` equal to `None`.
- The indentation of `return` matters: outside the loop it runs once at the end, inside it would stop at the first round.
- A function should handle its edge cases: for an empty list I return `None`, meaning "no average exists".
- A `return` exits the function immediately, so no `else` is needed after it.