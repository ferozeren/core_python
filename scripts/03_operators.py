# %% [markdown]
# # Python Operators
#
# Operators are used to perform operations on variables and values.
# Run this script directly in terminal:
# python 03_operators.py

# %%
# Basic Arithmetic Operators
print("\n--- Arithmetic Operators ---")

# Operators work on literal values, variables, or combinations of both.
print(10 + 5)  # 15

sum1: int = 100 + 50  # 150 (100 + 50)
sum2: int = sum1 + 250  # 400 (150 + 250)
sum3: int = sum2 + sum2  # 800 (400 + 400)

print(sum1, sum2, sum3)

# Core arithmetic operations:
# + (Addition), - (Subtraction), * (Multiplication), ** (Exponentiation)
print(10 - 3)  # 7
print(4 * 3)  # 12
print(2**3)  # 8 (2 raised to the power of 3)


# %%
# Division: True Division (/) vs Floor Division (//)
print("\n--- True Division (/) vs Floor Division (//) ---")

# Regular / True Division (/) ALWAYS returns a float, even when dividing two integers.
# Note: Always use forward slashes (/ or //). A backslash (\) is a line-continuation character and raises SyntaxError.
print(4.0 / 2.0)  # 2.0
print(2.5 / 0.5)  # 5.0
print(1 / 2)  # 0.5

# Floor Division (//) rounds DOWN toward negative infinity to the nearest whole number.
# Returns an int if both operands are ints; returns a float if either operand is a float.
print(4 // 2)  # 2
print(7 // 3)  # 2
print(7 // 4)  # 1 (1.75 rounded down)
print(1 // 2)  # 0

print(4.0 // 2.0)  # 2.0
print(7.0 // 4)  # 1.0
print(7 // 4.5)  # 1.0

# Floor Division with Negative Numbers:
# Because // rounds down toward negative infinity (-2 < -1.5), negative results move further below zero.
print(-3 / 2)  # -1.5
print(-3 // 2)  # -2 (rounds down to -2, NOT toward zero like -1)


# %%
# Division Edge Cases: Zero, Booleans, and Large Integers
print("\n--- Division Edge Cases ---")

# 1. ZeroDivisionError: Dividing by 0 (or False) raises ZeroDivisionError.
try:
    val: int = 10
    result: float = (1 + 2) / (val - 10)  # ZeroDivisionError: division by zero
    print(result)
except ZeroDivisionError as exc:
    print(exc)

# 2. Booleans in Division: True is treated as 1, False is treated as 0.
print(True / True)  # 1.0
print(False / True)  # 0.0
try:
    True / False  # Raises ZeroDivisionError!
except ZeroDivisionError as exc:
    print(exc)

# 3. Extreme Integer Values:
# Float division (/) has limited precision (~15-17 digits) and approximates huge numbers.
# Integer floor division (//) uses arbitrary-precision integers and stays 100% exact.
print(10**60 / 3)  # 3.3333333333333335e+59 (float approximation)
print(10**60 // 3)  # Exact 60-digit integer!
print(10**60 % 3)  # 1 (exact remainder)

# Common real-world formulas:
# hours = minutes / 60          (Unit conversion)
# speed = distance / time       (Rates)
# page = index // page_size     (Pagination)
# bin_idx = value // bin_size   (Data binning into 0-9, 10-19, etc.)


# %%
# Modulo Operator (%) & Modular Arithmetic
print("\n--- Modulo Operator (%) ---")

# Modulo (%) returns the remainder left over after floor division (//).
# Python guarantees the identity: a == b * (a // b) + (a % b)

print(7 % 2)  # 1 (7 // 2 is 3, with 1 left over)
print(8 % 2)  # 0 (even number -> remainder 0)
print(100 % 3)  # 1
print(90 % 60)  # 30 (e.g., 90 minutes = 1 hour and 30 minutes remaining)

# Verifying the modular arithmetic identity: a == b * (a // b) + (a % b)
print(2 * (7 // 2) + (7 % 2))  # 7

# Checking Even or Odd with % 2 (0 = Even, 1 = Odd)
row_number: int = 4
row_color: str = "light_gray" if row_number % 2 == 0 else "white"
print(f"Row {row_number} color: {row_color}")


# %%
# Modulo with Floats & Precision Gotchas
print("\n--- Modulo with Floats ---")

# If either operand is a float, % returns a float.
print(6.5 % 2)  # 0.5
print(7.5 % 4)  # 3.5
print(7 % 4.5)  # 2.5

# Floating-point representation gotcha:
# 0.3 / 0.1 in binary float is ~2.9999999999999996 (just under 3).
# So 0.3 // 0.1 floors down to 2.0, leaving a remainder of ~0.1 instead of 0.0!
print(0.3 // 0.1)  # 2.0
print(0.3 % 0.1)  # 0.09999999999999998


# %%
# Modulo with Negative Numbers, divmod(), and math.fmod()
print("\n--- Negative Modulo, divmod(), and math.fmod() ---")

import math  # noqa: E402

# In Python, the result of `a % b` ALWAYS matches the sign of the DIVISOR (b).
# In C, Java, and JS, `%` matches the sign of the dividend (a) because they truncate toward zero.
print(-5 % 3)  # 1  (because -5 == 3 * (-2) + 1; stays in range [0, 3))
print(5 % -3)  # -1 (divisor is negative, so remainder is negative)

# Cyclical wrap-around (works seamlessly even with negative offsets):
current_minute: int = 5
offset: int = -15
minute: int = (current_minute + offset) % 60  # (-10) % 60 -> 50
print(f"Wrapped minute: {minute}")

# divmod(a, b) returns a tuple of (a // b, a % b) in a single call.
print(divmod(7, 4))  # (1, 3)
print(divmod(7, 4.5))  # (1.0, 2.5)
print(divmod(-5, 3))  # (-2, 1)

# math.fmod(a, b) calculates the float remainder using C-style truncation toward zero,
# where the result sign matches the DIVIDEND (a) instead of the divisor (b).
print(math.fmod(-5, 3))  # -2.0


# %%
# Practical Modulo Use Cases: Cycling, Time Conversion, and Leap Years
print("\n--- Practical Modulo Use Cases ---")

# Round-robin / cycling through a list safely without IndexError:
servers: list[str] = ["Server1", "Server2", "Server3"]
for request_id in range(5):
    assigned = servers[request_id % len(servers)]
    print(f"Request {request_id} -> {assigned}")

# Converting total seconds into hours, minutes, and seconds using divmod():
total_seconds: int = 10_000
minutes, seconds = divmod(total_seconds, 60)
hours, minutes = divmod(minutes, 60)
print(f"{total_seconds}s = {hours}h {minutes}m {seconds}s")


# Leap Year Check: divisible by 4, except centuries (100) unless also divisible by 400.
def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


print(f"Is 1924 a leap year? {is_leap_year(1924)}")  # True


# %%
# Assignment Operators & The Ternary Conditional Expression
print("\n--- Ternary Conditional Expression ---")

# Compound assignment operators update a variable in place:
counter: int = 10
counter += 5  # Same as: counter = counter + 5
counter *= 2  # Same as: counter = counter * 2
print(f"counter: {counter}")  # 30

# Ternary Operator (Conditional Expression / Shorthand If):
# Syntax: value_if_true if condition else value_if_false
num: int = 6
day_type: str = "WEEKEND!" if num > 5 else "Workday"
print(day_type)

# Chained ternary expression (shorthand for if / elif / else):
day_label: str = (
    "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday"
)
print(day_label)


# %%
# Comparison Operators & Chaining
print("\n--- Comparison Operators ---")

# Comparison operators return True or False:
# == (Equal), != (Not equal), > (Greater), < (Less), >= (Greater/equal), <= (Less/equal)
x: int = 5
y: int = 3

print(x == y)  # False
print(x != y)  # True
print(x > y)  # True
print(x < y)  # False
print(x >= y)  # True
print(x <= y)  # False

# Chaining Comparison Operators:
# Python lets you chain comparisons naturally like mathematical intervals.
print(1 < x < 10)  # True (same as: 1 < x and x < 10)
print(1 < x and x < 10)  # True


# %%
# Logical Operators: and, or, not
print("\n--- Logical Operators (and, or, not) ---")

# and: True if BOTH operands are true
# or:  True if AT LEAST ONE operand is true
# not: Inverts the truth value, ALWAYS returning a bool (True -> False, False -> True)

val: int = 5
print(val > 0 and val < 10)  # True
print(val < 5 or val > 10)  # False
print(not (val > 3 and val < 10))  # False


# %%
# Logical `not` & Truthiness
print("\n--- Logical `not` & Truthiness ---")

# Falsy values in Python:
# False, None, 0, 0.0, 0j, "", [], {}, (), set(), range(0)
# Almost everything else is Truthy.

print(not True)  # False
print(not False)  # True

# Using `if not` is the Pythonic way to check for empty strings, lists, or None
# (preferred over `if len(collection) == 0:` or double negatives like `if not x != 1:`).
queue: list[str] = []
while not queue:
    print("Queue is empty, adding task_1...")
    queue.append("task_1")

# Using `not` as a guard clause before a `match` statement (Python 3.10+):
command: str = ""
if not command:
    print("No command provided.")
elif not command.isalpha():
    print("Invalid command format.")
else:
    match command.lower():
        case "start":
            print("Process starting.")
        case "stop":
            print("Process stopping.")
        case _:
            print("Unknown command.")


# %%
# Logical `or` with Non-Booleans, Default Values, and Short-Circuiting
print("\n--- Logical `or`: Non-Booleans & Short-Circuiting ---")

# With non-Boolean operands, `or` evaluates left-to-right and returns the FIRST truthy value,
# or the LAST value if all operands are falsy.
print(0 or 1)  # 1  (first truthy value)
print(12 or 21)  # 12 (first truthy value; stops immediately)
print(0 or [])  # [] (both are falsy, so returns the last operand)

# Setting fallback defaults with `or`:
# Note: Any falsy value ("", 0, False) triggers the fallback.
# If 0 or "" is a valid input, check `if x is None` explicitly instead of using `or`.
raw_username: str = ""
user_name: str = raw_username or "Guest"
print(f"Welcome, {user_name}!")


# Short-Circuit Evaluation:
# `or` stops evaluating as soon as it finds a truthy value.
# `and` stops evaluating as soon as it finds a falsy value.
def is_divisible_by_two(n: int) -> bool:
    print(f"Checking if {n} is divisible by 2")
    return n % 2 == 0


def is_divisible_by_five(n: int) -> bool:
    print(f"Checking if {n} is divisible by 5")
    return n % 5 == 0


# Because is_divisible_by_two(10) is True, is_divisible_by_five(10) is NEVER called!
print(is_divisible_by_two(10) or is_divisible_by_five(10))


# %%
# Common Logical Operator Pitfalls
print("\n--- Logical Operator Pitfalls ---")

# Pitfall 1: Incomplete Comparisons
# `x == 1 or 2` is evaluated as `(x == 1) or 2` because `==` has higher precedence than `or`.
# Since `2` is truthy, `(x == 1) or 2` ALWAYS returns `True` or `2`!
test_val: int = 3
print(test_val == 1 or 2)  # Prints 2 (Bug!)
print(test_val == 1 or test_val == 2)  # False (Correct)
print(test_val in (1, 2))  # False (Cleaner & Pythonic)

# Pitfall 2: Logical (`not`, `and`, `or`) vs Bitwise (`~`, `&`, `|`) in NumPy / pandas
# `not`, `and`, `or` require a single truth value and raise `ValueError: The truth value of a Series is ambiguous` on arrays.
# In NumPy/pandas, use elementwise bitwise operators (`~`, `&`, `|`) wrapped in parentheses:
# e.g., (df["age"] > 35) | (df["name"] == "Steve") or ~df["col"].isna()


# %%
# Identity Operators: is, is not
print("\n--- Identity Operators (is, is not) ---")

# `is` checks if two variables point to the EXACT same object in memory.
# `==` checks if the values inside the objects are equal.

box_x: list[str] = ["apple", "banana"]
box_y: list[str] = ["apple", "banana"]
box_z: list[str] = box_x

print(box_x is box_z)  # True: same object in memory
print(box_x is box_y)  # False: two separate list objects in memory
print(box_x == box_y)  # True: contents are equal
print(box_x is not box_y)  # True: not the same object


# %%
# Membership Operators: in, not in
print("\n--- Membership Operators (in, not in) ---")

# `in` and `not in` test whether a value or substring exists inside a collection/sequence.
# Compound forms (`x not in y` and `x is not y`) are always preferred over `not (x in y)`.

fruits: list[str] = ["apple", "banana", "cherry"]
print("banana" in fruits)  # True
print("pineapple" not in fruits)  # True

# Membership in Strings (case-sensitive substring check):
text: str = "Hello World"
print("H" in text)  # True
print("hello" in text)  # False (case-sensitive)
print("z" not in text)  # True


# %%
# Bitwise Operators
print("\n--- Bitwise Operators ---")

# Bitwise operators act on integers bit-by-bit in binary:
# 6 in binary = 0110
# 3 in binary = 0011

print(6 & 3)  # 2  (AND: 0110 & 0011 = 0010 -> sets bit to 1 if BOTH bits are 1)
print(6 | 3)  # 7  (OR:  0110 | 0011 = 0111 -> sets bit to 1 if AT LEAST ONE bit is 1)
print(6 ^ 3)  # 5  (XOR: 0110 ^ 0011 = 0101 -> sets bit to 1 if ONLY ONE bit is 1)
print(~6)  # -7 (NOT: inverts all bits; in two's complement, ~x == -x - 1)
print(3 << 2)  # 12 (Left shift:  0011 << 2 = 1100 -> shifts bits left, filling with 0s)
print(8 >> 2)  # 2  (Right shift: 1000 >> 2 = 0010 -> shifts bits right)


# %%
# Operator Precedence (PEMDAS & Logical Hierarchy)
print("\n--- Operator Precedence ---")

# Precedence order from highest to lowest:
# 1. ()                           Parentheses (innermost first)
# 2. **                           Exponentiation
# 3. +x, -x, ~x                   Unary plus, unary minus, bitwise NOT
# 4. *, /, //, %                  Multiplication, division, floor division, modulo
# 5. +, -                         Addition and subtraction
# 6. <<, >>                       Bitwise shifts
# 7. &                            Bitwise AND
# 8. ^                            Bitwise XOR
# 9. |                            Bitwise OR
# 10. ==, !=, >, >=, <, <=,
#     is, is not, in, not in      Comparisons, identity, and membership
# 11. not                         Logical NOT
# 12. and                         Logical AND
# 13. or                          Logical OR

# Multiplication (*) happens before addition (+):
print(100 + 5 * 3)  # 115

# Parentheses override precedence:
print((6 + 3) - (6 + 3))  # 0

# Step-by-step PEMDAS:
# 6 + (5 - 1) / 2 ** 2  ->  6 + 4 / 2 ** 2  ->  6 + 4 / 4  ->  6 + 1.0  ->  7.0
print(6 + (5 - 1) / 2**2)  # 7.0
print((6 + (5 - 1)) / 2**2)  # 2.5

# Same-precedence operators evaluate left-to-right (except ** which is right-to-left):
print(5 + 4 - 7 + 3)  # 5
print(5 + 4 * 2 % 3 - 1)  # 6  (4 * 2 = 8 -> 8 % 3 = 2 -> 5 + 2 - 1 = 6)

# Comparisons happen BEFORE `not`, and `not` happens before `and`, which happens before `or`:
print(not 8 > 4)  # False -> evaluated as: not (8 > 4)
print(not True and False)  # False -> evaluated as: (not True) and False
print(True or False and False)  # True  -> evaluated as: True or (False and False)


# %%
# Script Execution
print("\n--- Script Execution ---")


def main() -> None:
    print("Finished running 03_operators.py.")


if __name__ == "__main__":
    main()
