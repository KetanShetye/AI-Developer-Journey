# Operator 
# An operator is a symbol or function that tells the interpreter to perform a specific operation on one or more values (operands).
# An operator is a special symbol or keyword in Python used to perform operations on data values or variables, like arithmetic, comparison, assignment, logic, bitwise operations, and more.

# Operands 
# values on which operation is performed

# -> Arithmetic Operators
# Used for mathematical operations.
# | Operator | Description        | Example  | Result |
# | -------- | ------------------ | -------- | ------ |
# | `+`      | Addition           | `2 + 3`  | `5`    |
# | `-`      | Subtraction        | `5 - 2`  | `3`    |
# | `*`      | Multiplication     | `3 * 4`  | `12`   |
# | `/`      | Division (float)   | `7 / 2`  | `3.5`  | always returns float (even if both are int)
# | `//`     | Floor Division     | `7 // 2` | `3`    | Always returns whole number (even if both ar float) eg :- 5,5.0
# | `%`      | Modulo (remainder) | `7 % 2`  | `1`    |
# | `**`     | Exponentiation     | `2 ** 3` | `8`    |
a = 2 + 3
print(a)  # Output: 5
b = 5 - 2
print(b)  # Output: 3
c = 3 * 4
print(c)  # Output: 12
d = 7 / 2
print(d)  # Output: 3.5
e = 7 // 2
print(e)  # Output: 3
f = 7.0 // 2.0
print(f)  # Output: 3.0 (still float but floored)
g = 7 % 2
print(g)  # Output: 1
h = 2 ** 3
print(h)  # Output: 8


# -> Comparison Operator or Relational Operator
# used for Compare two values.
# | Operator | Description      | Example  | Result  |
# | -------- | ---------------- | -------- | ------- |
# | `==`     | Equal            | `5 == 5` | `True`  |
# | `!=`     | Not Equal        | `5 != 3` | `True`  |
# | `>`      | Greater Than     | `5 > 3`  | `True`  |
# | `<`      | Less Than        | `5 < 3`  | `False` |
# | `>=`     | Greater or Equal | `5 >= 5` | `True`  |
# | `<=`     | Less or Equal    | `5 <= 3` | `False` |
a = 5 == 5
print(a)  # Output: True
b = 5 != 3
print(b)  # Output: True
c = 5 > 3
print(c)  # Output: True
d = 5 < 3
print(d)  # Output: False
e = 5 >= 5
print(e)  # Output: True
f = 5 <= 3
print(f)  # Output: False

# -> Assignment Operator 
# Used to assign values to variables.
# | Operator | Description             | Equivalent To        |
# | -------- | ----------------------- | -------------------- |
# | `=`      | Assign                  | `x = 5`              |
# | `+=`     | Add and assign          | `x += 3 → x = x + 3` |
# | `-=`     | Subtract and assign     | `x -= 2 → x = x - 2` |
# | `*=`     | Multiply and assign     | `x *= 4`             |
# | `/=`     | Divide and assign       | `x /= 2`             |
# | `//=`    | Floor divide and assign | `x //= 3`            |
# | `%=`     | Modulo and assign       | `x %= 2`             |
# | `**=`    | Exponent and assign     | `x **= 2`            |
x = 5
print(x)  # Output: 5
x += 3  # Same as: x = x + 3
print(x)  # Output: 8
x -= 2  # Same as: x = x - 2
print(x)  # Output: 6
x *= 4  # Same as: x = x * 4
print(x)  # Output: 24
x /= 2  # Same as: x = x / 2
print(x)  # Output: 12.0 (always float)
x //= 5  # Same as: x = x // 5
print(x)  # Output: 2
x %= 4  # Same as: x = x % 4
print(x)  # Output: 3
x **= 2  # Same as: x = x ** 2
print(x)  # Output: 9


# -> Logical Operators
# Used to combine conditional statements.
# | Operator | Description           | Example           |
# | -------- | --------------------- | ----------------- |
# | `and`    | True if both are True | `x > 2 and x < 5` |
# | `or`     | True if one is True   | `x < 1 or x > 3`  |
# | `not`    | Negates the result    | `not(x > 3)`      |
x = 4
result = x > 2 and x < 5
print(result)  # Output: True
x = 1
result = x < 1 or x > 3
print(result)  # Output: False
x = 4
result = x < 1 or x > 3
print(result)  # Output: True
x = 4
result = not (x > 3)
print(result)  # Output: False

# -> Bitwise Operators
# Operate on bits (binary level).
# | Operator | Description | Binary Example      | Result |     |     |
# | -------- | ----------- | ------------------- | ------ | --- | --- |
# | &      | AND         | `5 & 3 → 101 & 011` | `1`    |     |     | Returns 1 only if both bits are 1.
# | `       | `          | OR                  | \`5    | 3\` | `7` |
# | ^      | XOR         | `5 ^ 3`             | `6`    |     |     |
# | ~      | NOT         | `~5`                | `-6`   |     |     |
# | <<     | Left Shift  | `5 << 1`            | `10`   |     |     |
# | >>     | Right Shift | `5 >> 1`            | `2`    |     |     |
# NOTE :- 
# ~x is equal to -x - 1 because Python uses 2's complement representation.
# Negative shift amounts will raise an error.
# Bitwise AND `&`
a = 5       # Binary: 0101  
b = 3       # Binary: 0011  
result = a & b
print(result)  # Output: 1
# 0101 & 0011 = 0001 (which is 1)
# Bitwise Or `|`
a = 5       # Binary: 0101  
b = 3       # Binary: 0011  
result = a | b
print(result)  # Output: 7
# 0101 | 0011 = 0111 (which is 7)

# Bitwise XOR `^`
# Returns 1 only if bits are different.
a = 5       # Binary: 0101  
b = 3       # Binary: 0011  
result = a ^ b
print(result)  # Output: 6
# 0101 ^ 0011 = 0110 (which is 6)

# Bitwise NOT `~`
# Inverts all bits. In Python, ~x equals -x - 1.
a = 5
result = ~a
print(result)  # Output: -6
# Because: ~5 = -(5) - 1 = -6

# Left Shift <<
# Shifts bits to the left (adds zeroes on the right).
a = 5       # Binary: 0101  
result = a << 1
print(result)  # Output: 10
# 0101 << 1 = 1010 (which is 10)

# Right Shift >>
# Shifts bits to the right (removes bits from the right).
a = 5       # Binary: 0101  
result = a >> 1
print(result)  # Output: 2
# 0101 >> 1 = 0010 (which is 2)


# -> Identity Operators
# Checks memory location.
# | Operator | Description             | Example      |
# | -------- | ----------------------- | ------------ |
# | `is`     | True if same object     | `x is y`     |
# | `is not` | True if not same object | `x is not y` |
# NOTE :- 'is' is not the same as '=='. 'is' checks identity (memory), '==' checks value.

# -> Membership Operators
# Test for presence in a sequence (like list, tuple, set, string).
# | Operator | Description       | Example              |
# | -------- | ----------------- | -------------------- |
# | `in`     | True if found     | `'a' in 'apple'`     |
# | `not in` | True if not found | `'z' not in 'apple'` |

# -> Ternary Operators 
# result = a if condition else b
age = 24
status = "Adult" if age >= 18 else "Minor"

# -> Operator Overloading
# Python lets you override operators in your own classes using special methods (magic methods).
# | Operator | Magic Method           |
# | -------- | ---------------------- |
# | `+`      | `__add__(self, other)` |
# | `-`      | `__sub__`              |
# | `*`      | `__mul__`              |
# | `/`      | `__truediv__`          |
# | `//`     | `__floordiv__`         |
# | `%`      | `__mod__`              |
# | `**`     | `__pow__`              |
# | `<`      | `__lt__`               |
# | `>`      | `__gt__`               |
# | `==`     | `__eq__`               |
# | `!=`     | `__ne__`               |
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"

    # Addition: v1 + v2
    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        return NotImplemented

    # Subtraction: v1 - v2
    def __sub__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x - other.x, self.y - other.y)
        return NotImplemented

    # Multiplication: v1 * scalar (only scalar for simplicity)
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector2D(self.x * other, self.y * other)
        return NotImplemented

    # True Division: v1 / scalar
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector2D(self.x / other, self.y / other)
        return NotImplemented

    # Floor Division: v1 // scalar
    def __floordiv__(self, other):
        if isinstance(other, (int, float)):
            return Vector2D(self.x // other, self.y // other)
        return NotImplemented

    # Modulo: v1 % scalar
    def __mod__(self, other):
        if isinstance(other, (int, float)):
            return Vector2D(self.x % other, self.y % other)
        return NotImplemented

    # Exponentiation: v1 ** scalar
    def __pow__(self, other):
        if isinstance(other, (int, float)):
            return Vector2D(self.x ** other, self.y ** other)
        return NotImplemented

    # Less than: v1 < v2 (compare by vector magnitude)
    def __lt__(self, other):
        if isinstance(other, Vector2D):
            return self.magnitude() < other.magnitude()
        return NotImplemented

    # Greater than: v1 > v2
    def __gt__(self, other):
        if isinstance(other, Vector2D):
            return self.magnitude() > other.magnitude()
        return NotImplemented

    # Equal: v1 == v2
    def __eq__(self, other):
        if isinstance(other, Vector2D):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    # Not equal: v1 != v2
    def __ne__(self, other):
        eq_result = self.__eq__(other)
        if eq_result is NotImplemented:
            return NotImplemented
        return not eq_result

    def magnitude(self):
        return (self.x**2 + self.y**2) ** 0.5


# Usage Examples
v1 = Vector2D(2, 3)
v2 = Vector2D(4, 1)

print("v1 + v2 =", v1 + v2)           # Vector2D(6, 4)
print("v1 - v2 =", v1 - v2)           # Vector2D(-2, 2)
print("v1 * 3 =", v1 * 3)             # Vector2D(6, 9)
print("v2 / 2 =", v2 / 2)             # Vector2D(2.0, 0.5)
print("v2 // 2 =", v2 // 2)           # Vector2D(2, 0)
print("v1 % 2 =", v1 % 2)             # Vector2D(0, 1)
print("v1 ** 2 =", v1 ** 2)           # Vector2D(4, 9)

print("v1 < v2:", v1 < v2)            # Compare magnitude
print("v1 > v2:", v1 > v2)
print("v1 == v2:", v1 == v2)
print("v1 != v2:", v1 != v2)


# -> Chained Comparison
# 3 < x < 10 is equivalent to (3 < x) and (x < 10) 

# -> Walrus Operator (Python 3.8+)
# `:=`
# Allows assignment within expressions.
# if (n := len(data)) > 5:
#     print(f"{n} items")

# -> Callable Opearator
# `()`
# Used to call a function or a callable object.
def greet():
    return "Hello"

print(greet())  # '()' calls the function
# Also works with class instances if __call__() is defined.
class A:
    def __call__(self):
        print("I was called!")

a = A()
a()  # calls __call__

# -> Indexing Operator 
# `[]`
# Used to access individual elements in sequences like list, tuple, or string
# The index starts from 0
x = [1, 2, 3]
x[1]  # → 2 (accesses the element at index 1)
# Negative indices are also allowed:
x[-1]  # → 3 (last element)

# -> Slicing operator 
# Syntax: `<sequence>[<start_index>:<stop_index>:<step>]`
# Used to access a range of elements (a "slice") from a sequence.
x = [1, 2, 3, 4, 5]
x[1:4]     # → [2, 3, 4] (from index 1 to 3)
x[::2]     # → [1, 3, 5] (every second item)
x[::-1]    # → [5, 4, 3, 2, 1] (reversed list)


# -> Context Manager Operator 
# `with`
# Not an operator, but it internally uses: __enter__() , __exit__()

# -> Custome Operator Logic In Classes
# You can make your class behave like any built-in type by overriding magic methods. 
# Example:
class MyList:
    def __getitem__(self, index):
        return f"Index {index} accessed"
    
# ->  Summary Table of Magic Methods for Operators
# | Operator | Method         |
# | -------- | -------------- |
# | `+`      | `__add__`      |
# | `-`      | `__sub__`      |
# | `*`      | `__mul__`      |
# | `/`      | `__truediv__`  |
# | `//`     | `__floordiv__` |
# | `%`      | `__mod__`      |
# | `**`     | `__pow__`      |
# | `<`      | `__lt__`       |
# | `<=`     | `__le__`       |
# | `==`     | `__eq__`       |
# | `!=`     | `__ne__`       |
# | `>`      | `__gt__`       |
# | `>=`     | `__ge__`       |
# | `[]`     | `__getitem__`  |
# | `()`     | `__call__`     |
# | `in`     | `__contains__` |

