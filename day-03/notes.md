# Day 03

## What I did
- Learned how to repeat code with loops: `for` and `while`.
- Wrote loops.py (print 1 to 5, sum 1 to 10) and countdown.py (5 to 1).
- Used a variable that accumulates a value inside a loop (`total = total + i`).

## What I got wrong
- Left a useless line `i+1` in the loop: it calculates a value and throws it away.
- Predicted 5 for the sum of 1 to 5 (I looked at the last number, not the accumulated total), then 14 instead of 15.
- Almost forgot that a `while` loop needs a line that changes the condition, otherwise it never ends.

## What I understood
- `range(1, 6)` starts at 1 and stops before 6: the first number is included, the last is not.
- A `for` loop changes `i` by itself, a `while` loop needs me to change the variable.
- Without decreasing `n`, the condition `n > 0` stays true forever: that is an infinite loop, and Ctrl+C stops it.
- Tracing a loop round by round in a table shows what it really does.
- Pairing numbers from the ends (1+10, 2+9, ...) gives the sum 55 without a loop.