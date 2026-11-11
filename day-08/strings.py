# Day 08 - strings

text = "  The Quick Brown Fox  "

# Exercise 1: remove outer spaces and make everything lowercase.
# String methods return a NEW string, the original `text` does not change.
print(text.lower().strip())           # the quick brown fox

# Exercise 2: split into words, then print them in reverse order.
words = text.split()                  # ['The', 'Quick', 'Brown', 'Fox']
print(words)
# The text BEFORE the dot is the glue placed between the items.
print(" ".join(reversed(words)))      # Fox Brown Quick The


# Exercise 3: palindrome, ignoring case and spaces.
def is_palindrome(s):
    s = s.lower().replace(" ", "")    # clean the text once
    return s == s[::-1]               # [::-1] walks the string backwards


print(is_palindrome("Never odd or even"))   # True
print(is_palindrome("Hello"))               # False
print(is_palindrome(""))                    # True (empty reversed is empty)


# Exercise 4: count the vowels (case does not matter).
def count_vowels(s):
    count = 0                         # counter starts at zero
    for c in s.lower():               # one character at a time
        if c in "aeiou":              # True only for vowels
            count += 1
    return count


print(count_vowels("Hello world"))    # 3
print(count_vowels(""))               # 0

# Exercise 5: f-string, variables go inside {}.
name = "Jack"
age = 25
print(f"{name} is {age} years old")   # Jack is 25 years old