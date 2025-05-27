# String Slicing
# Slicing allows you to extract a portion (substring) of a string.
# string[start:end:step]
s = "Hello, World!"

print(s[0:5])     # 'Hello'
print(s[:5])      # 'Hello'
print(s[7:])      # 'World!'
print(s[-6:-1])   # 'World'
print(s[::-1])    # '!dlroW ,olleH' (reverse)

#  String Formatting
# Python offers several ways to format strings.

#  f-Strings (Python 3.6+)
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")

# str.format()
print("My name is {} and I am {} years old.".format(name, age))
# using index numbers  
print("The {0} is {1} and the {1} is {0}.".format("sky", "blue")) # The sky is blue and the blue is sky.
# using variable names
print("Hello {name}, your balance is {balance}.".format(name="Bob", balance=500)) # Hello Bob, your balance is 500.
#  Formatting Numbers
pi = 3.14159265
print("Value of pi is {:.2f}".format(pi)) # Value of pi is 3.14
print("My score is {:.1f}".format(92.678)) # My score is 92.7
# :.2f means:
# : → Start formatting instructions
# .2 → Show 2 digits after the decimal
# f → Format the number as a float (decimal number)


# % Formatting (older style)
print("My name is %s and I am %d years old." % (name, age))

# Other Useful Operations

#  Length of a string
len(s)

#  String Concatenation
"Hello" + " " + "World"  # 'Hello World'

# String Repetition
"Ha" * 3   # 'HaHaHa'