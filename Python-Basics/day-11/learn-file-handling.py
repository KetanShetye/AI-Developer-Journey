# File Handling
# File handling is used to read, write, append, or modify files stored on disk.
# Python provides built-in functions for working with files.

# open()
# Opening a File
file = open("example.txt", "mode")
# | Mode | Meaning                       | File Exists | File Created | Truncates? |
# | ---- | ----------------------------- | ----------- | ------------ | ---------- |
# | `r`  | Read                          | ✅           | ❌            | ❌          |
# | `w`  | Write (overwrites)            | ✅/❌         | ✅            | ✅          |
# | `a`  | Append                        | ✅/❌         | ✅            | ❌          |
# | `x`  | Create (fails if file exists) | ❌           | ✅            | ❌          |
# | `r+` | Read + Write                  | ✅           | ❌            | ❌          |
# | `w+` | Write + Read (overwrites)     | ✅/❌         | ✅            | ✅          |
# | `a+` | Append + Read                 | ✅/❌         | ✅            | ❌          |


# Reading a File
file = open("example.txt", "r")
# Read the entire file
content = file.read()
# Read line by line
line1 = file.readline()
# Read all lines into a list
lines = file.readlines()
file.close()

# Writing to a File
file = open("example.txt", "w")
file.write("This will overwrite the file.\n")
file.write("Second line.")
file.close()

# Use "a" mode to append instead of overwrite:
file = open("example.txt", "a")
file.write("This will be added to the end.")
file.close()

#  Using with Statement (Recommended)
# Automatically handles closing the file.
with open("example.txt", "r") as file:
    content = file.read()
    print(content)


with open("example.txt", "w") as file:
    file.write("New content.")
# No need to call file.close() – handled automatically

# 5. File Object Methods
# read(size)
# Reads the specified number of bytes (or characters in text mode).
with open("example.txt", "r") as f:
    data = f.read(10)  # Read first 10 characters
    print(data)
# readline()
# Reads the next line from the file (including \n).
with open("example.txt", "r") as f:
    line = f.readline()
    print("First line:", line)

# readlines()
# Reads all lines and returns a list of strings.
with open("example.txt", "r") as f:
    lines = f.readlines()
    print(lines)  # List of all lines in the file

# write(string)
# Writes a string to the file. If the file is opened in write mode, it overwrites by default.
with open("example.txt", "w") as f:
    f.write("Hello, world!\n")
    f.write("This is a second line.")

# writelines(list)
# Writes a list of strings to the file. Newline characters (\n) must be included manually.
lines = ["First line\n", "Second line\n", "Third line\n"]

with open("example.txt", "w") as f:
    f.writelines(lines)

# seek(offset)
# Moves the file pointer (cursor) to the specified byte offset.
with open("example.txt", "r") as f:
    f.seek(5)  # Move to 6th character (index starts from 0)
    print(f.read())  # Read from there onward

# tell()
# Returns the current file pointer position (in bytes from the start).
with open("example.txt", "r") as f:
    print("Position:", f.tell())  # Initially 0
    f.read(5)
    print("After reading 5 chars, position:", f.tell())

# close()
# Closes the file and releases system resources. Not required when using with, but here's how it's used manually:
f = open("example.txt", "r")
data = f.read()
f.close()


# Check if File Exists
import os

if os.path.exists("example.txt"):
    print("File exists.")
else:
    print("File does not exist.")

# Delete a File
import os
os.remove("example.txt")


# Working with Directories
import os
# Make directory
os.mkdir("new_folder")
# List files
print(os.listdir("."))
# Change directory
os.chdir("new_folder")
# Remove directory (only if empty)
os.rmdir("new_folder")

# Handling Exceptions
try:
    with open("data.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")
except IOError:
    print("IO error occurred")

# Read & Write JSON Files
import json

# Write JSON
data = {"name": "Alice", "age": 25}
with open("data.json", "w") as file:
    json.dump(data, file)

# Read JSON
with open("data.json", "r") as file:
    loaded_data = json.load(file)

# Read & Write CSV Files
import csv

# Write CSV
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age"])
    writer.writerow(["Alice", 25])

# Read CSV
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# File Pointer (tell() and seek())
with open("example.txt", "r") as f:
    print(f.tell())  # Position
    f.seek(5)         # Move to 5th byte
    print(f.read())   # Read from that position

# File Permissions (Advanced)
# You can set file permissions using os.chmod (Unix systems):
import os
os.chmod("example.txt", 0o644)  # Read-write for owner, read for others

#  Reading Large Files in Chunks
with open("large.txt", "r") as file:
    while True:
        chunk = file.read(1024)  # Read 1 KB
        if not chunk:
            break
        print(chunk)  # process chunk here

# Detect File Type (Optional)
# Use libraries like mimetypes:

import mimetypes

file_type, _ = mimetypes.guess_type("example.jpg")
print(file_type)  # e.g., image/jpeg