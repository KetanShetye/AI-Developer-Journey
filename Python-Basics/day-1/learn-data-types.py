
# Data Types
# 1. int 
# -> Represents whole numbers
# -> 10, -10, 0
age=24

# 2.float
# -> Represents decimal (floating-point) numbers
# -> 3.14, 1.3, -1.0, 0.0
height=5.7

# 3.str
# -> Represents a sequence of characters (text) 
# -> "hello" 'hello'
name="ketan"

# 4.bool
# -> Represents truth values
# -> True, False
isReadyToLearnPython = True

# 5.list 
# -> Ordered, changeable collection of items 
# -> [1,2,3]
fruits = ["apple", "banana", "cherry"]
print(fruits[1])         # Output: banana
fruits.append("mango")   # Add an item
print(fruits)            # Output: ['apple', 'banana', 'cherry', 'mango']

# 6.tuple
# -> Ordered, unchangeable collection 
# -> (1,2,3)
coordinates = (10, 20)
print(coordinates[0])    # Output: 10
# coordinates[1] = 30    # ❌ Error: tuples are immutable

# 7.set
# -> Unordered collection of unique items
# -> {1,2,3}
unique_numbers = {1, 2, 3, 2, 1}
print(unique_numbers)    # Output: {1, 2, 3}
unique_numbers.add(4)    # Add an item
print(unique_numbers)    # Output: {1, 2, 3, 4}

# 8.dict
# -> Collection of key-value pairs
# {"name": "Alice"}
student = {
    name: "Ketan",
    "name":"Vilas",
    "age": 24,
    "isEnrolled": True
}
print(student[name])   # Output: Ketan
print(student["name"]) # Output: Vilas
student["age"] = 25       # Update value
print(student)           # Output: {'name': 'Ketan', 'age': 25, 'isEnrolled': True}
