# input()
# -> function reads a line of text entered by the user.
# -> It always returns a string, even if the user enters a number.
name = input("Enter your name: ")
print("Hello", name)

age = input("Enter your age: ")
print("your", age) # even if user enters no. its data type will be string

# Type Conversion
age = int(input("Enter your age: "))  # Convert input to integer
height = float(input("Enter your height: "))  # Convert input to float


# split()
# Using split() to Take Multiple Inputs
x, y = input("Enter two numbers: ").split()
print(x, y)

# Type Conversion with Multiple Inputs
x, y = map(int, input("Enter two numbers: ").split())
print(x,y)

# Custom Separator
a, b, c = input("Enter three words separated by comma: ").split(',')
print(a, b, c)


# print()
print("Hello, World!")

#  Printing Multiple Items
name = "Alice"
age = 25
print("Name:", name, "Age:", age)

# Separator 
# `sep`
print("Python", "Java", "C++", sep=". ")# Output: Python. Java. C++

# End Character 
# `end`
print("Hello", end=" ")
print("World!")
# Output: Hello World!

#  Formatted Strings (f-strings)
name = "Bob"
score = 95.5
print(f"{name} scored {score}%")

# -> Escape Characters

# \n – New line
print("Hello\nWorld")
# Hello
# World

# \t – Tab
print("Name:\tJohn")
print("Age:\t25")
# Name:   John
# Age:    25

# \\ – Backslash
print("This is a backslash: \\")
# This is a backslash: \

# \" – Double quote
print("He said, \"Python is awesome!\"")
# He said, "Python is awesome!"

# \' – Single Quote
print('It\'s a beautiful day!')
# It's a beautiful day!

# \r – Carriage Return (returns the cursor to the beginning of the line)
print("12345\rABC")
# ABC45

# \b – Backspace (removes the character before it)
print("Helloo\b!")
# Hello!

# \a – Bell/Alert (produces a beep sound in some terminals)
print("Warning\a")
# Warning
# And may hear a beep (depends on your system/terminal).

# \f – Form Feed (rarely used, moves to the next page in printers)
print("Hello\fWorld")
# HelloWorld
# It may appear as a strange symbol or have no effect.

# \v – Vertical Tab (rarely used)
print("Hello\vWorld")
# HelloWorld
# May show as a vertical spacing depending on the console.

#  Printing without New Line
print("Hello", end="")
print("World")
# Output: HelloWorld