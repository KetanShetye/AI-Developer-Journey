
# 🐍 Python Day 9 – Practice Questions

## 🟢 Beginner Level Questions


1. What is the syntax to define a function in Python?
2. Write a function that prints "Welcome to Python!"
3. How do you call a function named show_message?
4. Write a function greet_user(name) that prints "Hello, <name>"
5. What is the purpose of the return statement in a function?
6. Create a function add(a, b) that returns the sum of a and b
7. What happens if you define a function but forget to call it?
8. Write a function print_even(num1, num2) that prints both numbers only if they are even
9. What are positional arguments? Give an example
10. What are default parameters? Write a function with one

---

## 🟡 Intermediate Level Questions

1. Write a function multiply(a=2, b=3) and call it with positional arguments, keyword arguments, and no arguments
2. Explain the difference between positional and keyword arguments with examples
3. Write a function calculate_total(*args) that returns the total of all numbers passed
4. Create a function user_info(**kwargs) that prints name and age if present
5. What will be the output of:
   def test(a, b=10):
   return a + b
   print(test(5))
6. Modify the function to allow infinite positional arguments and print their squares
7. What is the data type of args and kwargs inside a function?
8. Can a function return multiple values? Show with an example
9. Create a function display_data(name, *args, **kwargs) that prints all data nicely
10. What's wrong with this code? Fix it:
    def my_func(name, age=30, country):
    print(name, age, country)

---

## 🔴 Advanced Level Questions

1. Write a function that behaves differently if only 1 argument is passed vs multiple
2. What happens if you use both *args and **kwargs but in the wrong order?
3. Create a function that takes a list of names using *args and a greeting using **kwargs
4. How do default parameters interact with *args?
5. Create a function process_items(*args, reverse=False) where reverse is a keyword-only argument
6. How would you pass a dictionary into a function expecting **kwargs?
7. Write a function that takes a required param, then *args, then a default keyword param, then **kwargs
8. Demonstrate how *args can be used to unpack a list into a function
9. Write a function that sums only even numbers passed via *args
10. Can we modify a global variable inside a function? Show with return and without using global
