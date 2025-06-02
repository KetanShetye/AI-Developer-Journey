# Function Annotations
# Function Annotations allow you to attach metadata to a function’s parameters and return value using colons : and arrows ->.
# 🔹 They don’t enforce types, but help with:
# Code readability
# IDE autocompletion
# Type checking with tools like mypy, pylint, or modern IDEs

#  Syntax of Annotations
# def function_name(param1: type1, param2: type2) -> return_type:
#     ...
# eg:-
def greet(name: str) -> str:
    return "Hello, " + name
# This says:
# name should be a str
# Function will return a str
# But:
# Python will NOT stop you if you pass an int (annotations are not enforced).

# Using Annotations Without Enforcing
def add(a: int, b: int) -> int:
    return a + b

print(add(5, 3))       # ✅ 8
print(add("5", "3"))   # ✅ 53 (No error — annotations ignored by default)

# Custom Annotations (with metadata)
# You can even use descriptive annotations, not just types:
# Option 1: Use string literals but disable the Pylance warning for that line
# You can ignore it if you want just a descriptive annotation:

def process(data: "JSON string", retries: int = 3) -> bool:
    return True
# Then in VSCode, you can suppress the warning manually or just ignore it because it’s harmless.

# Option 2:
from typing import Annotated

def process(data: Annotated[str, "JSON string"], retries: int = 3) -> bool:
    return True
# This way, data is typed as str but with an extra annotation "JSON string", and tools won’t complain.

# Option 3:
JSON = str  # alias for documentation and type hinting

def process(data: JSON, retries: int = 3) -> bool:
    return True
# Now Pylance knows what JSON is and won’t give an error.

# Access Annotations Programmatically
# Annotations are stored in the function’s __annotations__ dictionary.
def area(radius: float) -> float:
    return 3.14 * radius * radius

print(area.__annotations__)
# Output: {'radius': <class 'float'>, 'return': <class 'float'>}

# With Complex Types (using typing module)
from typing import List, Dict

def total(marks: List[int]) -> int:
    return sum(marks)

def get_profile() -> Dict[str, str]:
    return {"name": "Ketan", "role": "Developer"}

# Enforcing Annotations (Optional)
# Python itself does not enforce annotations.
# But tools like mypy can:
# pip install mypy
# mypy your_file.py

# Summary
# | Feature        | Description                                    |
# | -------------- | ---------------------------------------------- |
# | Purpose        | Add type hints to parameters and return values |
# | Syntax         | `param: type`, `-> return_type`                |
# | Runtime Impact | None (no enforcement)                          |
# | Tools          | Used by `mypy`, linters, IDEs                  |
