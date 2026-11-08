# First loop: print the numbers from 1 to 5
# range(1, 6) starts at 1 and stops before 6
for i in range(1, 6):
    print(i)

# Second loop: sum the numbers from 1 to 10
# total starts at 0 and collects the sum while the loop runs
total = 0
# range(1, 11) starts at 1 and stops before 11
for i in range(1, 11):
    # Add the current number to the running total
    total = total + i
# This print has no indentation: it runs once, after the loop is finished
print("Sum from 1 to 10:", total)