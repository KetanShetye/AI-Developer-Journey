# Tuples 
# A tuple is a collection of ordered and immutable elements in Python. 
# It can hold elements of different data
my_tuple = (1, "hello", 3.14)

#  Tuple Characteristics
# | Feature                  | Description                      |
# | ------------------------ | -------------------------------- |
# | **Ordered**              | Elements maintain their order    |
# | **Immutable**            | Cannot be changed after creation |
# | **Allows Duplicates**    | Can contain duplicate values     |
# | **Can Hold Mixed Types** | E.g., int, str, float, etc.      |


# Creating Tuples
# Empty tuple
t1 = ()
# Tuple with elements
t2 = (1, 2, 3)
# Tuple without parentheses (not recommended)
t3 = 1, 2, 3
# Single-element tuple (note the comma)
t4 = (10,)

# Accessing Tuple Elements
t = (10, 20, 30, 40)
# Indexing
print(t[0])      # 10
print(t[-1])     # 40
# Slicing
print(t[1:3])    # (20, 30)


#  Tuple Operations
t1 = (1, 2)
t2 = (3, 4)

# Concatenation
print(t1 + t2)          # (1, 2, 3, 4)

# Repetition
print(t1 * 2)           # (1, 2, 1, 2)

# Membership
print(2 in t1)          # True

# Length
print(len(t1))          # 2

for item in (1, 2, 3):
    print(item)


# Tuple Methods
t = (1, 2, 2, 3)

print(t.count(2))   # 2
print(t.index(3))   # 3

# Tuple Packing and Unpacking
# Packing
t = 1, 2, "A"

# Unpacking
a, b, c = t
print(a, b, c)  # 1 2 A

# Nested Tuples
t = (1, (2, 3), 4)

print(t[1])       # (2, 3)
print(t[1][0])    # 2

# Tuples vs Lists
# | Feature     | Tuple                    | List         |
# | ----------- | ------------------------ | ------------ |
# | Syntax      | `(1, 2, 3)`              | `[1, 2, 3]`  |
# | Mutability  | Immutable                | Mutable      |
# | Methods     | Fewer (`count`, `index`) | Many methods |
# | Performance | Faster                   | Slower       |
# | Use Cases   | Fixed data               | Dynamic data |


# When to Use Tuples?
# When your data should not change.
# For function returns with multiple values.
# As dictionary keys (tuples are hashable).
# For faster performance compared to lists.

#  Tuple as Dictionary Keys
d = {(1, 2): "value"}
print(d[(1, 2)])     # value

# Advanced: Named Tuples
from collections import namedtuple

Point = namedtuple("Point", "x y")
p = Point(1, 2)

print(p.x, p.y)   # 1 2

