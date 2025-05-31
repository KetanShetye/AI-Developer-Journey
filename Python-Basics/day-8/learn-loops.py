# Loops
# A loop is used to repeat a block of code multiple times until a certain condition is met.

# `for` Loop
# Used to iterate over a sequence (like a list, tuple, dictionary, set, or string).
# for variable in sequence:
#     # code to execute
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# `while` Loop
# Repeats as long as a condition is true.
# while condition:
#     # code to execute
count = 0
while count < 5:
    print(count)
    count += 1

# Loop Control Statements
# `break` - Stops the loop entirely.
for i in range(10):
    if i == 5:
        break
    print(i)
# `continue` - Skips the rest of the code inside the loop for the current iteration and moves to the next iteration.
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # prints only odd numbers

# `else` with Loops
# The `else` block executes after the loop finishes normally (without a `break`).
# NOTE - If `break` occurs, `else` is skipped.
for i in range(3):
    print(i)
else:
    print("Loop completed without break")

# Looping Over Different Data Structures
# List
lst = [1, 2, 3]
for num in lst:
    print(num)

# String
for char in "hello":
    print(char)

# Dictionary (keys, values, items)
d = {'a': 1, 'b': 2}
for key in d:
    print(key)

for value in d.values():
    print(value)

for key, value in d.items():
    print(key, value)


# Nested Loops
# Loops inside loops.
for i in range(3):
    for j in range(2):
        print(i, j)

# Looping with range()
# range(start, stop, step) generates a sequence of numbers.
for i in range(5):  # 0 to 4
    print(i)

for i in range(2, 10, 2):  # 2, 4, 6, 8
    print(i)

#  Using enumerate() in Loops
# To get index and value during iteration.
names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names):
    print(index, name)

#  List Comprehensions (Loop + Expression in one line)
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# Infinite Loops
# A while loop that never ends (usually needs break inside).
while True:
    response = input("Enter 'exit' to stop: ")
    if response == 'exit':
        break

# NOTE
# Use for loops when you want to iterate over known sequences or fixed numbers.
# Use while loops when you want to repeat something until a condition is met, and the number of iterations may not be known upfront.

# Run a loop 5 times: Prefer for with range
# Iterate over a list of items:
for fruit in ["apple", "banana", "cherry"]:
    print(fruit)

# Keep asking user for input until they type "exit": Use while
while True:
    command = input("Enter command: ")
    if command == "exit":
        break

# Run a loop 5 times: Prefer for with range
for i in range(5):
    print(i)

# Wait until a certain variable reaches a value (dynamic condition): Use while
count = 0
while count < 5:
    print(count)
    count += 1


# | Use Case                                                                            | Recommended Loop | Why?                                                                            |
# | ----------------------------------------------------------------------------------- | ---------------- | ------------------------------------------------------------------------------- |
# | You want to iterate over a fixed collection (list, string, dictionary, range, etc.) | **`for` loop**   | It directly works on iterable objects, concise and readable.                    |
# | You want to repeat code until a condition changes dynamically                       | **`while` loop** | Good for unknown iterations where the end condition is dynamic or input-driven. |
# | You know exactly how many times to repeat (fixed number)                            | **`for` loop**   | Easier with `range()` for a known count.                                        |
# | You want to keep repeating until some event happens (e.g., user input)              | **`while` loop** | Condition can be checked each time, allowing flexible exit.                     |
