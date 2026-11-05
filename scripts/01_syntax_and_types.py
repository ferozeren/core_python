my_number: int = 10  # Integer

my_string: str = "Python is so 'Great'"  # String - Double quotes
also_string: str = 'Rust is also "Great"'  # String - Single quotes


# Multi Line Strigs - Triple quotes
also_string: str = """This is multi
lines string
it can also used for docstrings.
"""


# Function
def greet(name: str) -> None:
    # Doc String
    """Prints a personalized greeting message to the console.

    Args:
        name: Name of the person to greet.

    """
    print(f"Hello, {name}")


greet("Feroze")  # Function Caller

# Decimal
decimal: float = 3.14159


apple_cost: float = 8.3

orange_cost: float = 1.2

banana_cost: float = 12.3

# Mutli Line Statments

fruit_costs: float = apple_cost + orange_cost + banana_cost

days: list[str] = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


# Multi Line Comment, not official

"""
This is multi
line Comment
"""

# None


# Multiple Statement on a single line

# import sys; x = "foo"; sys.stdout.write(x + "\n")


# Multiple Statement Groups as Suites


my_list: list[str] = ["John", "Kevin", "Jereme", "Ali", "Paul", "Arjun", "Lee"]

if len(my_list) >= 10:
    print("Pretty Big List of names")
elif len(my_list) >= 5:
    print("Big List of names")
else:
    print("Small Array of names")


# Blank lines
input("\n\nPress the enter key to exit.")  # Wating for the user input
