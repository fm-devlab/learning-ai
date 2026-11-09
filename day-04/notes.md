# Day 04

## What I did
- Learned how to store many values in one variable with lists.
- Wrote lists.py (indexing, len, append, looping) and stats.py (sum, average, min, max).
- Used `for number in numbers` to loop directly over a list.

## What I got wrong
- Wrote `numbers[0,4]` to get the first and last element: an index takes only one position.
- Got a sum of 14 instead of 15 in the previous loop exercise because I skipped a step in the table.

## What I understood
- List positions start at 0, and `numbers[-1]` always points to the last element, even if the list grows.
- `numbers[10]` on a short list raises an IndexError: the last valid position is `len(numbers) - 1`.
- `append` adds an element at the end and changes the original list.
- `total += number` is the short form of `total = total + number`.
- The `/` operator always returns a float, even when the division is exact (`18.0`).