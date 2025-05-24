# Python 

# -> high-level programming language 
# Easy for humans to read, write, and understand
# Abstracts away hardware details (like memory, registers, CPU instructions), 

# -> interpreted programming language 
# Code is executed line-by-line by an interpreter at runtime,
# Code is not compiled into a separate executable beforehand.
# The Python interpreter handles:
# 1.Syntax checking
# 2.Code execution
# 3.Error reporting (immediately when it finds them)
# eg :- When you write and run Python code like this:
print("Hello")
x = 5 + 3
print(x)
# Python does not compile it into machine code first like C or Java.
# Instead, the Python interpreter reads and executes one line at a time:
# Read print("Hello") → execute it
# Read x = 5 + 3 → execute it
# Read print(x) → execute it
# Behind the scenes, 
# Python does compile your code to bytecode (.pyc files), 
# but this is still interpreted by the Python Virtual Machine (PVM), 
# not a true compiled binary like in C or Java.
# 🟩 Your Python Code (hello.py)
#      |
#      |    (1) You run the file
#      v
# 🟦 Python Interpreter (CPython)
#      |
#      |    (2) Reads and executes line-by-line
#      v
# 🟨 Python Virtual Machine (PVM)
#      |
#      |    (3) Converts to bytecode & runs it
#      v
# 🖥️ Final Output (on screen)

# -> Step-by-Step of Python Execution (Simplified):
# You run python hello.py
# Python converts the code into bytecode (.pyc)
# Bytecode is fed to the Python Virtual Machine (PVM)
# PVM executes it line-by-line
# You see the output immediately!


# -> C v/s Python
# | Compiled Language                                  | Interpreted Language                          |
# | -------------------------------------------------- | --------------------------------------------- |
# | Uses compiler                                      | Uses interpreter                              |
# | Converts code to machine language before execution | Executes line-by-line during runtime          |
# | Faster execution after compiling                   | Slower (but simpler for testing and learning) |
# | Generates an `.exe` or binary                      | No binary file needed                         |

# ->| Concept     | Java                          | Python                        |
# | ----------- | ----------------------------- | ----------------------------- |
# | Source Code | `.java` file                  | `.py` file                    |
# | Compilation | Compiled to bytecode `.class` | Compiled to bytecode `.pyc`   |
# | Runtime     | JVM (Java Virtual Machine)    | Python Interpreter (CPython)  |
# | Execution   | JVM runs bytecode             | Interpreter executes bytecode |

# ->Python doesn’t need a separate compiler. 
# You write Python code, 
# and the interpreter handles everything—compiling, executing, and managing memory.

# ->Analogy: Interpreter vs Compiler
# Imagine You’re at the United Nations
# 🧍 You (Python programmer) speak Hindi
# 🧑 Interpreter: Translates line-by-line from Hindi to English
# 🧑‍⚖️ Audience: Understands only English
# ➤ Interpreter
# You speak a Hindi sentence → Interpreter translates it → Audience hears it
# You speak next sentence → Interpreter translates → Audience hears it
# Repeat...
# ➡️ This is how Python works (interpreted): line-by-line translation and execution.
# ➤ Compiler
# You give a whole speech in Hindi written on paper → Translator takes time to convert the entire speech into English → Audience gets the whole translated copy and reads it
# ➡️ This is how C or Java works (compiled): whole program is converted into machine language first, then executed.


# known for its simplicity, readability, and versatility. 
# It was created by Guido van Rossum and first released in 1991.

# ->Features 
# | Feature                    | Description                                                                |
# | -------------------------- | -------------------------------------------------------------------------- |
# | **Simple & Readable**      | Python code is close to plain English.                                     |
# | **Interpreted Language**   | Code runs line-by-line (no separate compilation step).                     |
# | **Dynamically Typed**      | You don't need to declare variable types (e.g., `a = 5`, not `int a = 5`). |
# | **Object-Oriented**        | Everything is an object; supports classes and inheritance.                 |
# | **High-Level Language**    | You don’t manage memory manually or worry about hardware-level details.    |
# | **Portable**               | Python code can run on Windows, macOS, Linux with no changes.              |
# | **Large Standard Library** | Comes with built-in modules for web, OS, file I/O, math, etc.              |
# | **Extensible**             | Easily integrates with other languages like C/C++, Java, etc.              |
# | **Huge Community**         | Millions of developers and tons of third-party packages.                   |

# ->What Can You Build with Python?
# | Area                     | Examples                                |
# | ------------------------ | --------------------------------------- |
# | **Web Development**      | Django, Flask                           |
# | **Data Science**         | Pandas, NumPy, Matplotlib, scikit-learn |
# | **Machine Learning/AI**  | TensorFlow, PyTorch                     |
# | **Scripting/Automation** | File handling, system scripts           |
# | **Game Development**     | Pygame                                  |
# | **Mobile Apps**          | Kivy, BeeWare                           |
# | **Desktop Apps**         | Tkinter, PyQt                           |


# ->Fun Fact
# The name “Python” doesn't come from the snake!
# It was inspired by the British comedy show "Monty Python’s Flying Circus".