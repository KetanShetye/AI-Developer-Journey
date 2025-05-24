# Type Conversion 
# -> changing a value from one data type to another.

# 1. Implicit Type Conversion 
# -> Automatic - Python automatically converts data types when it makes sense (safe conversions).
a = 10          # int
b = 3.5         # float
result = a + b  # int + float = float
print(result)   # 13.5
print(type(result))  # <class 'float'> 
# no data loss

# 2. Explicit Type Conversion 
# -> Manually - Programmer manually convert data types using Python's built-in functions.

# -> int() Converts to integer
s = "100"
n = int(s)
print(n + 1)          # 101


# -> float() Converts to float 
value = "3.14"
pi = float(value)
print(pi + 1)         # 4.14


# -> str() Converts to string
x = 25
y = str(x)
print(y)              # "25"
print(type(y))        # <class 'str'>


# -> bool() Converts to boolean
print(bool(0))        # False
print(bool(1))        # True
print(bool(""))       # False
print(bool("hello"))  # True


# -> list() Converts to list
s = "abc"
print(list(s))   # ['a', 'b', 'c']


# -> tuple() Converts to tuple
s = "abc"
print(tuple(s))  # ('a', 'b', 'c')


# -> set() Converts to set
s = "abc"
print(set(s))    # {'a', 'b', 'c'} (order may vary)


# Note not all conversions are safe 
s = "abc"
# int(s)       # ❌ Error: Cannot convert letters to int

x = 5.99
print(int(x))    # 5 (not 6)


