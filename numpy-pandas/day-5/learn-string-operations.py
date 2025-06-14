# String Operations with .str
# String Operations in Pandas using the powerful .str accessor 
# must-know for data cleaning, preprocessing, and analysis.
# In Pandas, the .str accessor allows vectorized string functions on Series of string or mixed types (usually object dtype).

# Basic String Methods
# df['col'].str.lower()     # Convert to lowercase
# df['col'].str.upper()     # Convert to uppercase
# df['col'].str.title()     # Capitalize each word
# df['col'].str.strip()     # Remove leading/trailing whitespace
# df['col'].str.replace('old', 'new')  # Replace substrings

# Searching & Matching
# df['col'].str.contains('abc')         # Boolean Series
# df['col'].str.startswith('A')         # Starts with A
# df['col'].str.endswith('Z')           # Ends with Z
# df['col'].str.match(r'^[A-Z][a-z]+$') # Regex pattern matching

# Splitting & Extracting

# split()
# df['col'].str.split('-')           # Split into list
# df['col'].str.split('-', expand=True)  # Split into multiple columns

# get()
# df['col'].str.split().str.get(0)   # Get first word

# extract() – Regex groups into columns
# df['col'].str.extract(r'(\d+)-([A-Z]+)')

#  Length & Count
# df['col'].str.len()               # Length of each string
# df['col'].str.count('a')          # Count of substring

# Conditional String Operations

# df[df['name'].str.contains('John')]
# df[df['email'].str.endswith('@gmail.com')]

import pandas as pd

data = {
    'Name': [' Alice ', 'BOB', 'charlie'],
    'Email': ['alice@gmail.com', 'bob@yahoo.com', 'charlie@gmail.com']
}

df = pd.DataFrame(data)

# Strip whitespaces and convert to proper case
df['Name'] = df['Name'].str.strip().str.title()

# Check which emails are Gmail
df['IsGmail'] = df['Email'].str.endswith('@gmail.com')

# Extract username from email
df['Username'] = df['Email'].str.extract(r'(^[^@]+)')


# Handling Missing Values
# .str functions automatically return NaN for missing values. You can use:
# df['col'].str.lower().fillna('')
# | Method                   | Description                 |
# | ------------------------ | --------------------------- |
# | `.str.lower() / upper()` | Case conversion             |
# | `.str.strip()`           | Trim spaces                 |
# | `.str.contains()`        | Check for substring         |
# | `.str.startswith()`      | Starts with pattern         |
# | `.str.endswith()`        | Ends with pattern           |
# | `.str.replace(old, new)` | Replace text                |
# | `.str.len()`             | String length               |
# | `.str.count('a')`        | Count substring occurrences |
# | `.str.split()` / `get()` | Split string and get part   |
# | `.str.extract(regex)`    | Extract groups using regex  |
