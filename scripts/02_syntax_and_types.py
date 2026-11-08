# %% [markdown]
# # Interactive Mode vs Script Mode

# %% [markdown]
# # Interactive Mode (REPL):
# # Open a terminal and type:
# # python
# #
# # You can execute Python statements directly.
# #
# # >>> print("Hello, World!")
# #
# # Script Mode:
# # Write Python code in a .py file and run it:
# # python 01_syntax_and_types.py

# %%
# Python Identifiers: names used for variables, functions, classes, etc.
print("\n--- Python Identifiers ---")

# Type annotations are hints for linters/IDEs; the interpreter does not enforce them.
my_number: int = 10  # (type: int)
my_name: str = "Feroze"  # (type: str)

# Valid identifiers
user_name: str = "Adam"
_private_variable: int = 100  # Single underscore: convention for internal/private use
__strong_private_variable: int = (
    100_000  # Note: Name mangling only occurs inside classes, not modules
)

number1: int = 50
myVariable: str = "Python"  # Allowed, but snake_case is PEP 8 standard for variables

# Python is case-sensitive.
name: str = "John"
Name: str = "Alex"

print(name)
print(Name)

# Invalid identifiers:
# 1number = 10       # Cannot start with a number (digit)
# my-name = "John"   # Hyphens are not allowed (treated as minus operators)
# my name = "John"   # Spaces / whitespace are not allowed
# class = "Python"   # Reserved keyword

# %%
# PEP 8 Python Naming Conventions

# Variables and functions use snake_case.
user_name: str = "Feroze"

# Constants use UPPER_SNAKE_CASE (Convention).
MAX_SIZE: int = 100
PI: float = 3.14159  # Better: math.pi

# Class names use PascalCase (UpperCamelCase).
# Example: class UserProfile:


# %%
# Python Reserved Keywords
print("\n--- Reserved Keywords ---")

# Keywords have special meanings in Python.
# They cannot be used as variable or function names.

import keyword  # noqa: E402

print(keyword.kwlist)

# Check whether a name is a keyword.
print(keyword.iskeyword("if"))
print(keyword.iskeyword("hello"))


# %%
# Variables & Object References
print("\n--- Variables & Multiple Assignments ---")

my_number: int = 10
my_string: str = "Python is so 'Great'"
also_string: str = 'Rust is also "Great"'

# Multiple Assignments (Unpacking)
x, y, z = 10, 20, 30

# Chained assignment (all reference the same object in memory)
p = q = r = 100

print(x, y, z)
print(p, q, r)


# %%
# Data Types
print("\n--- Core Primitive Data Types ---")

# Core Built-in Primitive types
# Note: bool is a subclass of int (isinstance(True, int) is True, and True + True == 2)

number: int = 10
decimal: float = 3.14
text: str = "Hello, Python!"
is_valid: bool = True
nothing: None = None
complex_number: complex = 2 + 3j

print(type(number))
print(type(decimal))
print(type(text))
print(type(is_valid))
print(type(nothing))
print(type(complex_number), complex_number)
print(type(complex_number.real), complex_number.real)  # Float
print(type(complex_number.imag), complex_number.imag)  # Float

# %%
# Arbitrary-Precision Integers (No Max Int) & sys.maxsize
print("\n--- Arbitrary-Precision Integers & sys.maxsize ---")

# Unlike C, C++, Rust, or Java (which use fixed-width types like int8, int32, int64 that can overflow),
# Python's `int` has arbitrary precision: it dynamically allocates more memory as numbers grow,
# limited only by available system RAM.

import math  # noqa: E402
import sys  # noqa: E402

# sys.maxsize is NOT the maximum integer value in Python.
# It is the max value of CPython's internal Py_ssize_t (2**63 - 1 on 64-bit, 2**31 - 1 on 32-bit),
# which limits maximum container/list lengths and indices—not integer arithmetic.
print(f"sys.maxsize (64-bit Py_ssize_t limit): {sys.maxsize}")
print(f"sys.maxsize + 1 (no overflow!):        {sys.maxsize + 1}")
print(f"2**100:                                {2**100}")

# %%
# Built-in Functions for Large Integers & Common Pitfalls
print("\n--- Large Integer Functions (pow, isqrt, factorial) & Pitfalls ---")

# pow(base, exp, mod): Supports fast modular exponentiation without building huge intermediates.
print(f"pow(3, 2):             {pow(3, 2)}")  # 9
print(f"pow(3, 2, 2):          {pow(3, 2, 2)}")  # 9 % 2 = 1
print(
    f"pow(2, 10_000_000, 17): {pow(2, 10_000_000, 17)}"
)  # Instant modular exponentiation -> 1

# math.isqrt(n): Exact integer square root (floor of sqrt) without float range limits.
print(f"math.isqrt(27):        {math.isqrt(27)}")  # 5
print(f"math.isqrt(10**100):   {math.isqrt(10**100)}")  # 10**50 exact integer

# math.factorial(n): Computes exact factorials for large numbers.
print(f"math.factorial(5):     {math.factorial(5)}")  # 120
print(f"Digits in 1000!:       {len(str(math.factorial(1000)))}")  # 2568 digits

# Pitfall float('inf') is a float, NOT an integer.
# Passing float('inf') to range(), math.isqrt(), or math.factorial() raises TypeError.
# Converting int(float('inf')) raises OverflowError.
pos_inf: float = float("inf")
print(f"float('inf') type: {type(pos_inf)} | 10**100 type: {type(10**100)}")

# Pitfall: Data Science Libraries (NumPy & pandas) use fixed-width integers!
# Unlike built-in Python `int`, NumPy/pandas default to fixed-width types (np.int8, np.int32, np.int64)
# for memory and C-level speed, which CAN overflow (e.g., np.int8(127) + 1 wraps around to -128).


# %%
# Precise Numeric Types (Requires Imports)
print("\n--- Precise Numeric Types ---")

from decimal import Decimal  # noqa: E402
from fractions import Fraction  # noqa: E402

# High-precision numeric types (e.g., Decimal("0.1") + Decimal("0.2") gives exact 0.3)
precise_decimal: Decimal = Decimal("2.3")  # Avoid Decimal(2.3), use str '' | ""
rational_fraction: Fraction = Fraction(3, 4)

print(f"precise_decimal: {type(precise_decimal)}", precise_decimal)
print(f"rational_fraction: {type(rational_fraction)}", rational_fraction)

# %%
# Core Collection Types & Mutability Overview
print("\n--- Core Collection Types ---")

# Immutable: int, float, str, tuple, bytes, frozenset
# Mutable:   list, dict, set, bytearray

sequence_list: list[int | float] = [
    1,
    2,
    2.3,
]  # Mutable list (e.g., .append() modifies in-place)
immutable_tuple: tuple[str, int] = ("Age", 28)  # Immutable tuple
unique_set: set[int] = {1, 2, 3}  # Mutable set (automatically deduplicates elements)
mapping_dict: dict[str, int] = {"apples": 10, "kiwi": 23}  # Mutable key-value mapping
binary_bytes: bytes = b"Hello"  # Immutable bytes

print(f"sequence_list: {type(sequence_list)}", sequence_list)
print(f"immutable_tuple: {type(immutable_tuple)}", immutable_tuple)
print(f"unique_set: {type(unique_set)}", unique_set)
print(f"mapping_dict: {type(mapping_dict)}", mapping_dict)
print(f"binary_bytes: {type(binary_bytes)}", binary_bytes)

# %%
# Type Conversion & Casting
print("\n--- Type Conversion ---")

number: int = 10
decimal: float = float(number)

print(decimal)
print(type(decimal))

price: float = 19.99
whole_number: int = int(price)

print(whole_number)  # Truncates toward zero (removes the decimal part -> 19)

text_number: str = "100"
converted_number: int = int(text_number)

print(converted_number)
print(type(converted_number))

age: int = 21
age_string: str = str(age)

print(age_string)
print(type(age_string))


# %%
# Type Checking
print("\n--- Type Checking ---")

value: int = 100

print(type(value))
print(isinstance(value, int))
print(isinstance(value, str))


# %%
# Python Lines and Indentation
print("\n--- Lines and Indentation ---")

# Python uses indentation to define blocks of code (4 spaces per indentation level is PEP 8 standard).
# Unlike languages such as Cpp, Rust and Java, Python does not use curly braces.

statement: bool = True

if statement:
    print("Inside the if block")
    print("Both statements belong to the same block.")
else:
    print("Inside the else block.")

# Incorrect indentation causes an IndentationError.

# if True:
#     print("Hello")
#   print("World")

# IndentationError: unindent does not match any outer indentation level (<string>, line 19)
#   File <string>:19
#     print("World")
#                   ^
# IndentationError: unindent does not match any outer indentation level

# %%
# Multiple Statement Groups as Suites
print("\n--- Statement Suites ---")

# A suite is a group of statements (code block) that belong to
# a compound statement such as if, for, while, def or class.

my_list: list[str] = [
    "John",
    "Kevin",
    "Jereme",
    "Ali",
    "Paul",
    "Arjun",
    "Lee",
]

if len(my_list) >= 10:
    print("Pretty Big List of names")
elif len(my_list) >= 5:
    print("Big List of names")
else:
    print("Small List of names")


# %%
# Multi-line Statements
print("\n--- Multi-line Statements ---")

# Multi-line statement continuation using parentheses (preferred over \):

apple_cost: float = 8.3
orange_cost: float = 1.2
banana_cost: float = 12.3
kiwi_cost: float = 19.0
dragon_fruit_cost: float = 7.8
strawberry_cost: float = 2.3

fruit_costs: float = (
    apple_cost
    + orange_cost
    + banana_cost
    + kiwi_cost
    + dragon_fruit_cost
    + strawberry_cost
)

print(fruit_costs)

# Lists can also be written across multiple lines.

days: list[str] = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]

# Explicit line continuation using a backslash.

# total: int = 10  \
#              + 20 \
#              + 30


total: int = 10 + 20 + 30


print(total)

# Parentheses are generally preferred over backslashes
# because they make multi-line statements easier to maintain.


# %%
# Quotations & String Syntax in Python
print("\n--- Quotations in Python ---")

# Single quotes
single_quote: str = 'Hello, Python!'  # fmt: skip

# Double quotes
double_quote: str = "Hello, Python!"

# Quotes inside strings
my_string: str = "Python is so 'Great'"
also_string: str = 'Rust is also "Great"'

# Triple quotes span multiple lines and preserve linebreaks.
# Triple single quotes
triple_single: str = '''This is a
multi-line string.
'''  # fmt: skip

# Triple double quotes
triple_double: str = """This is also a
multi-line string.
"""

# Note: F-Strings (f"...") are the preferred string formatting in Python 3.6+
# Example: f"Item: {item:<10} | Cost: ${price:.2f}"

print(single_quote)
print(double_quote)
print(my_string)
print(also_string)
print(triple_single)
print(triple_double)


# %%
# Comments in Python
print("\n--- Comments ---")

# Single-line comments start with a #.

# This is a comment.

print("Hello, World!")  # Comment after a statement

# Multi-line comments can be written using multiple # symbols.

# This is a comment.
# This is another comment.
# This is also a comment.

# Triple-quoted strings are not technically comments.
# They are string literals, but are commonly used for
# documentation and docstrings.


# %%
# Docstrings
print("\n--- Docstrings ---")


def greet(name: str) -> None:
    """Prints a personalized greeting message.

    Args:
        name: Name of the person to greet.
    """

    print(f"Hello, {name}")


greet("Feroze")

# Accessing a function's docstring via metadata.
print(greet.__doc__)


# %%
# None (Python's Null)
print("\n--- None ---")

# Null represents missing information or the intentional absence of a value.
# In Python, null is labeled with the keyword `None` (of type `NoneType`).
# Note: Python 3.10+ uses `int | None` syntax; older code uses `Optional[int]` from `typing`.

has_value: int | None = None

if has_value:
    print(f"has_value is not empty! {has_value}")
elif has_value is None:
    print("has_value is None")

print(type(has_value))  # <class 'NoneType'>


# %%
# None is a Singleton & Truthiness Overview
print("\n--- None is a Singleton ---")

# A singleton is an object for which only one instance exists in memory.
# In Python, None is a singleton. Every variable assigned to None
# refers to the exact same memory object.
#
# Falsy values: None, False, 0, 0.0, "", [], (), {}, set(), range(0)
# Everything else is Truthy.

a: str | None = ""
b: str | None = None
c: str | None = None

print(f"Singleton check (b is c): {b is c}")  # True

# Testing the print statements
print(a == "", a is None)
print(b is None, "b has value" if b else "b is empty/None", "\n")


# 1. Truthiness Check
# Result: Does NOT print. Python treats "" as Falsy.
if a:
    print(f"1. If a: It holds a value! '{a}'")

# 2. None Check
# Result: WILL print. An empty string is still a valid object in memory (it is not None).
if a is not None:
    print(f"2. a is NOT None: It holds a object! (Even if it is empty: '{a}')")

# 3. Text/Empty Check (High performance, no memory allocation)
# Result: Does NOT print. The string contains no actual text characters.
if isinstance(a, str) and a and not a.isspace():
    print(f"3. a has real text: '{a}'")
else:
    print("3. a is empty or just whitespace!")

# %%
# '==' vs 'is', Equality vs Python Identity
print("\n--- '==' vs 'is' (Numbers) ---")

# == checks VALUE equality.
# 'is' / 'is not' checks MEMORY IDENTITY (same object in memory) or None.

# Simple numbers (Shared reference)
# When you assign a simple number, both variables point to the exact same value.
fruit_cost: int = 2
fruit_cost2: int = fruit_cost

print(f"Values: {fruit_cost}, {fruit_cost2}")
print(f"Equality (==): {fruit_cost == fruit_cost2}")  # True: Both are the number 2
print(
    f"Identity (is): {fruit_cost is fruit_cost2}"
)  # True: They look at the same spot in memory

# %%
# Lists (Two separate boxes)
print("\n--- '==' vs 'is' (Lists) ---")

# Think of lists as two identical boxes. They hold the exact same toys inside,
# but they are still two completely separate boxes sitting on the floor (different heap allocations).
list_a: list[int] = [1, 2, 3]
list_b: list[int] = [1, 2, 3]

print(f"Equality (==): {list_a == list_b}")  # True: The items inside match perfectly
print(
    f"Identity (is): {list_a is list_b}"
)  # False: They are two different boxes in memory (different heap allocations)

# %%
# The Golden Rule (Checking for None)
print("\n--- Checking for None ---")

# In Python, there is only ever one true "None" in the entire system (None is a singleton).
# Because of this, we always use "is None" or "is not None" instead of "== None".
# Custom objects can override `==` (__eq__), which can cause unexpected behavior,
# whereas `is` strictly checks memory identity.
some_name: str | None = None

print(
    f"Is None (is): {some_name is None}"
)  # True: The safest, most standard way to check
print(f"Is not None (is not): {some_name is not None}")  # False

# %%
# None as a Default Parameter Value
print("\n--- None as Default Parameter ---")


def greet_person(name: str | None = None) -> None:
    """Prints a greeting.

    If no name is provided, a generic greeting is used.
    """
    # 1. isinstance(name, str): Rejects None, 0, or any accidental non-string type.
    # 2. name: Catches completely empty strings ("").
    # 3. not name.isspace(): Catches blank-space strings ("   ") without allocating a new string object.
    if isinstance(name, str) and name and not name.isspace():
        print(f"Hi, {name}")
    else:
        print("Hi, there!")


greet_person("")
greet_person("   ")
greet_person("Adam")

# pyrefly: ignore[bad-argument-type]
greet_person(0)
greet_person(None)

# %%
# None as a Return Value
print("\n--- None as Return Value ---")

# Every Python function returns a value.
# Functions without an explicit return statement (or with a bare `return`)
# return None by default (common for side-effect functions like printing or writing files).

output: None = greet_person()

print(type(output))


# %%
# None in Lists & Dictionaries
print("\n--- None in Lists & Dictionaries ---")

user_names: list[str | None] = [
    "Adam",
    "Alex",
    "Benji",
    None,
    "Jimmy",
    "Lee",
]

print(user_names)  # Includes None

# Excluding None
print([name for name in user_names if name is not None])

# Replacing None with "Unknown"
print([name if name is not None else "Unknown" for name in user_names])

# None as a placeholder value in a Dictionary
user_profile: dict[str, str | None] = {
    "name": "Sarah",
    "subscription": "Pro",
    "phone": None,  # Field exists, but no phone number provided
}
print(f"User phone: {user_profile['phone']}")

# Empty List is Falsy (empty collections evaluate to False in boolean contexts) but not `None`

updated_names: list[str] = []

print(updated_names is None, updated_names)
if not updated_names:  # non-pythonic way, `if len(updated_names) == 0:`
    print("Updated Names List is Empty!")
else:
    print("It has something?")


# %%
# None vs NaN (Not a Number)
print("\n--- None vs NaN ---")

# None: NoneType, represents the general absence of a value (check with `is None`).
# NaN:  float, represents an undefined/unrepresentable numeric value (check with `math.isnan()`).

nan_value: float = float("nan")

print(f"nan_value: {nan_value} | type: {type(nan_value)}")
print(f"NaN == NaN: {nan_value == nan_value}")  # False! NaN is NEVER equal to itself
print(f"math.isnan(nan_value): {math.isnan(nan_value)}")  # True


# %%
# Best Practice: Guard Early, Don't Nest
print("\n--- Guard Clauses with None ---")

# Use guard clauses at the top of a function to handle None early
# rather than deeply nesting if-statements.


def apply_discount(price: float | None, category: str | None = None) -> float | None:
    # Guard clause: handle None immediately
    if price is None:
        return None

    if category == "luxury":
        return price * 0.9

    return price


print(f"Discounted luxury price: {apply_discount(100.0, category='luxury')}")
print(f"Missing price: {apply_discount(None)}")


# %%
# Common Bugs with None & How to Avoid Them
print("\n--- Common Bugs with None ---")

# Bug: Forgetting a `return` statement
# Performs calculation, but implicitly returns None because `return` is missing.


def multiply_buggy(x: int, y: int) -> None:
    result = x * y  # noqa: F841 (calculated, but never returned!)


print(f"Forgot return statement: {multiply_buggy(2, 3)}")  # Prints None instead of 6


# Bug: Chained method calls on None (AttributeError)
# dict.get() returns None when a key isn't found. Calling a string method on None crashes.

users_db: dict[int, str] = {1: "Sarah", 2: "Mike"}
missing_user: str | None = users_db.get(3)  # Returns None

# print(missing_user.upper())  # Raises AttributeError: 'NoneType' object has no attribute 'upper'

if missing_user is not None:
    print(missing_user.upper())
else:
    print("User 3 not found; avoided AttributeError on None.")


# %%
# Standard Classes (OOP Basics)
print("\n--- Standard Classes ---")

# Classes bundle data (attributes) and behavior (methods) together.
# Class names use PascalCase by convention.


class UserProfile:
    # Class attribute (shared across all instances)
    platform: str = "GitHub"

    def __init__(self, username: str, followers: int = 0) -> None:
        # Instance attributes (unique to each object)
        self.username: str = username
        self.followers: int = followers
        self._is_active: bool = True  # Protected by convention
        self.__api_token: str = (
            "secret_123"  # Private (name-mangled to _UserProfile__api_token)
        )

    def follow(self) -> None:
        """Instance method: modifies object state."""
        self.followers += 1

    def get_token_preview(self) -> str:
        """Accesses the private mangled attribute internally."""
        return f"{self.__api_token[:6]}***"

    def __repr__(self) -> str:
        """Developer-friendly string representation."""
        return f"UserProfile(username='{self.username}', followers={self.followers})"


user = UserProfile("Feroze", 10)
user.follow()

print(user)
print(f"Platform: {user.platform}")
print(f"Token preview: {user.get_token_preview()}")
# Accessing mangled name directly (discouraged, but shows how mangling works):
print(f"Mangled access: {user._UserProfile__api_token}")  # type: ignore[attr-defined]


# %%
# Dataclasses (Data-Oriented Classes)
print("\n--- Dataclasses ---")

# @dataclass automatically generates __init__, __repr__, and __eq__.
# Use frozen=True to make instances immutable (read-only).

from dataclasses import dataclass, field  # noqa: E402


@dataclass
class Product:
    name: str
    price: float
    in_stock: bool = True
    tags: list[str] = field(default_factory=list)  # Safe default for mutable types


@dataclass(frozen=True)
class Point3D:
    x: float
    y: float
    z: float = 0.0


item1 = Product("Mechanical Keyboard", 99.99, tags=["tech", "peripherals"])
item2 = Product("Mechanical Keyboard", 99.99, tags=["tech", "peripherals"])

print(item1)
print(
    f"Dataclass equality (==): {item1 == item2}"
)  # True: compares field values automatically

origin = Point3D(0.0, 0.0)
print(f"Frozen dataclass: {origin}")
# origin.x = 5.0  # Raises FrozenInstanceError


# %%
# NamedTuple (Lightweight Immutable Records)
print("\n--- NamedTuple ---")

# NamedTuple creates tuple subclasses with named fields.
# They are immutable, memory-efficient, and support tuple unpacking and indexing.

from typing import NamedTuple  # noqa: E402


class Color(NamedTuple):
    red: int
    green: int
    blue: int
    alpha: float = 1.0  # Default value


# sky_blue: Color = Color(135, 206, 235)
sky_blue: Color = Color(red=135, green=206, blue=235)

# Access by name or index
print(f"Color: {sky_blue}")
print(f"By name (red): {sky_blue.red} | By index [1] (green): {sky_blue[1]}")

# Unpacking like a regular tuple
red, green, blue, alpha = sky_blue
print(f"Unpacked: r={red}, g={green}, b={blue}, a={alpha}")


# %%
# Abstract Base Classes (ABCs)
print("\n--- Abstract Base Classes (ABC) ---")

# Abstract classes define a strict interface (contract) for subclasses.
# You cannot instantiate an abstract class directly; subclasses MUST implement all @abstractmethod methods.

from abc import ABC, abstractmethod  # noqa: E402


class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> str:
        """Must be implemented by any concrete subclass."""
        pass


class StripeProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> str:
        return f"Processed ${amount:.2f} via Stripe."


class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> str:
        return f"Processed ${amount:.2f} via PayPal."


# processor = PaymentProcessor()  # TypeError: Can't instantiate abstract class

stripe = StripeProcessor()
paypal = PayPalProcessor()

print(stripe.process_payment(49.99))
print(paypal.process_payment(19.50))
print(f"Is Stripe a PaymentProcessor? {isinstance(stripe, PaymentProcessor)}")


# %%
# Other Useful Class Types: Enum, TypedDict, and Protocol
print("\n--- Enum, TypedDict & Protocol ---")

from enum import Enum, auto  # noqa: E402
from typing import Protocol, TypedDict  # noqa: E402


# Enum: Defines a set of symbolic names bound to unique constant values.
class OrderStatus(Enum):
    PENDING = auto()
    SHIPPED = auto()
    DELIVERED = auto()


status = OrderStatus.SHIPPED
print(f"Enum: {status} | Name: {status.name} | Value: {status.value}")


# TypedDict: Adds static type checking for dictionaries with a fixed key structure.
# At runtime, it is just a normal Python dict.
class MovieRecord(TypedDict):
    title: str
    year: int
    rating: float


movie: MovieRecord = {"title": "Inception", "year": 2010, "rating": 8.8}
print(f"TypedDict (runtime dict): {movie} | Type: {type(movie)}")


# Protocol: Structural subtyping ("Duck Typing" for type checkers).
# Any class with a matching .render() method satisfies Renderable—no inheritance needed.
class Renderable(Protocol):
    def render(self) -> str: ...


class Button:
    def render(self) -> str:
        return "<button>Click Me</button>"


def draw_ui(element: Renderable) -> None:
    print(f"Rendered UI: {element.render()}")


draw_ui(Button())


# %%
# Multiple Statements on a Single Line

# Python allows multiple simple statements on one line
# using a semicolon.

# import sys; x = "foo"; sys.stdout.write(x + "\n")

# This is valid Python, but separate lines are easier to read.


# %%
# Script Execution (Script Entry Point Standard)
print("\n--- Script Execution ---")

# __name__ contains the name of the current module.
# When a file runs directly as a script, its value is "__main__".


def main() -> None:
    print("Running the Python script.")


if __name__ == "__main__":
    main()


# %%
# Command Line Arguments

# Command-line arguments are covered in a separate topic.
# They can be accessed using the sys or argparse modules.


# %%
# Blank Lines

# Blank lines help separate different sections of code.
# Python ignores lines containing only whitespace.

# Use blank lines to make your code easier to read.


# %%
# Waiting for User Input

# input() displays a prompt and waits for the user.

# The \n character creates a new line.

input("\n\nPress the Enter key to exit.")
