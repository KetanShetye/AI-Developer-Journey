# Dictionaries 
# A dictionary is an unordered, mutable (changeable), and indexed collection in Python. 
# It stores key-value pairs.
# Example
person = {
    "name": "Ketan",
    "age": 24,
    "location": "Maharashtra"
}

# Key concepts of Dictionaries 
# | Concept                | Description                                          | Example                   |
# | ---------------------- | ---------------------------------------------------- | ------------------------- |
# | **Keys & Values**      | Each item has a key and value                        | `"name": "Ketan"`         |
# | **Unordered**          | No fixed order of items                              | Cannot access by index    |
# | **Mutable**            | Can change, add or remove items                      | `dict["age"] = 25`        |
# | **Keys are unique**    | Duplicate keys are not allowed                       | Latest value is used      |
# | **Keys are immutable** | Only immutable types allowed (e.g., int, str, tuple) | `dict[{1,2}] = "error"` ❌ |

# Creating dictionaries 
# 1. Using curly braces
student = {"name": "Amit", "age": 21}

# 2. Using dict() constructor
student = dict(name="Amit", age=21)

# 3. Using zip
keys = ["a", "b"]
values = [1, 2]
zipped_dict = dict(zip(keys, values))


# Accessing and Modifying Items
person = {"name": "Ketan", "age": 24}

# Access
print(person["name"])        # Output: Ketan
print(person.get("age"))     # Output: 24

# Modify
person["age"] = 25

# Add new item
person["city"] = "Mumbai"

# Remove item
del person["city"]

# Looping Through a Dictionary
person = {"name": "Ketan", "age": 24}

# Keys
for key in person:
    print(key)

# Values
for value in person.values():
    print(value)

# Key-Value Pairs
for key, value in person.items():
    print(f"{key}: {value}")

# Dictionary Methods 
# | Method                          | Description                    | Example                       | Output               |
# | ------------------------------- | ------------------------------ | ----------------------------- | -------------------- |
# | `dict.clear()`                  | Removes all items              | `d.clear()`                   | `{}`                 |
# | `dict.copy()`                   | Returns a shallow copy         | `d.copy()`                    | Same content         |
# | `dict.fromkeys(keys, val)`      | Create new dict from keys      | `dict.fromkeys(['a','b'], 0)` | `{'a': 0, 'b': 0}`   |
# | `dict.get(key, default)`        | Returns value or default       | `d.get('x', 0)`               | `0`                  |
# | `dict.items()`                  | Returns list of (key, value)   | `d.items()`                   | `dict_items([...])`  |
# | `dict.keys()`                   | Returns list of keys           | `d.keys()`                    | `dict_keys([...])`   |
# | `dict.values()`                 | Returns list of values         | `d.values()`                  | `dict_values([...])` |
# | `dict.pop(key)`                 | Removes key & returns value    | `d.pop('a')`                  | Value of `'a'`       |
# | `dict.popitem()`                | Removes and returns last item  | `d.popitem()`                 | `(key, value)`       |
# | `dict.setdefault(key, default)` | Returns key's value or sets it | `d.setdefault('x', 5)`        | Value of `'x'`       |
# | `dict.update(dict2)`            | Adds items from another dict   | `d.update({'z':3})`           | Updated dict         |
# | `dict.__contains__('key')`      | Checks if key exists           | `'a' in d`                    | `True`/`False`       |


#  Dictionary Comprehensions
squares = {x: x**2 for x in range(5)}
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

#  Nested Dictionaries
students = {
    "Amit": {"age": 21, "grade": "A"},
    "Neha": {"age": 22, "grade": "B"}
}
print(students["Amit"]["grade"])  # Output: A

# Immutable Keys Only
# ✅ Keys must be immutable (unchangeable)
# ❌ You cannot use mutable (changeable) types like lists or other dictionaries as keys.
# Immutable means it cannot be changed after creation.
# | Immutable ✅ | Mutable ❌ |
# | ----------- | --------- |
# | `int`       | `list`    |
# | `str`       | `dict`    |
# | `float`     | `set`     |
# | `tuple`     |           |

# Valid Keys (Immutable types)
d = {
    1: "integer key",           # int
    "name": "string key",       # str
    (1, 2): "tuple key"         # tuple (as long as it contains only immutable items)
}
print(d[(1, 2)])  # ✅ Works

# Invalid Keys (Mutable types)
d = {
    [1, 2]: "list key"  # ❌ Error: list is mutable and unhashable
}
# Output:
# TypeError: unhashable type: 'list'

