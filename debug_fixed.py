"""
Debug Fixed — Part C Q3
Day 7 PM Assignment - IIT Gandhinagar

Original buggy code had 4 issues:
  Bug 1 — age was a raw string from input() — fixed: int(input(...))
  Bug 2 — Indentation error on if/else block — fixed: proper 4-space indent
  Bug 3 — Wrong variable in f-string: f"name is {age}" — fixed: f"{name} is {age}..."
  Bug 4 — Invalid format specifier f'{score:.0}' — fixed: f'{score:.0f}'
"""

name = input("Name: ")
age = int(input("Age: "))  # Bug 1 fixed: cast to int

if age >= 18:  # Bug 2 fixed: corrected indentation
    status = "Adult"
else:
    status = "Minor"

print(f"{name} is {age} years old and is a {status}")  # Bug 3 fixed: name var
print(f"In 5 years: {age + 5}")
score = 85.5
print(f"Score: {score:.0f}")  # Bug 4 fixed: added 'f' to format spec
