# Sorting and Filtering Data in Pandas
# crucial for refining, analyzing, and preparing data for reports or models.

# Sorting Data
# 📌 By Columns (Ascending/Descending)
# df.sort_values(by='column_name')                      # Ascending
# df.sort_values(by='column_name', ascending=False)     # Descending

# 📌 By Multiple Columns
# df.sort_values(by=['dept', 'salary'], ascending=[True, False])

# 📌 Sorting by Index
# df.sort_index()
# df.sort_index(ascending=False)

# Filtering Data (Boolean Masking)
# 📌 Basic Filtering
# df[df['age'] > 30]
# df[df['department'] == 'HR']

# 📌 Multiple Conditions
# df[(df['salary'] > 50000) & (df['department'] == 'IT')]
# df[(df['age'] < 25) | (df['experience'] > 5)]

# 📌 Using .isin() for Set Membership
# df[df['role'].isin(['Manager', 'Team Lead'])]

# 📌 Using .between() for Ranges
# df[df['salary'].between(40000, 80000)]

# 📌 Using .str.contains() for Text Match
# df[df['email'].str.contains('gmail')]

# Using .query() for SQL-like Filtering
# df.query("department == 'HR' and salary > 40000")

# Dropping Duplicates Before Sorting
# df.drop_duplicates().sort_values(by='name')

# Reordering Columns (Optional Sorting Aid)
# df[['name', 'age', 'salary']].sort_values(by='salary')

import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'department': ['HR', 'IT', 'HR', 'Finance', 'IT'],
    'salary': [50000, 70000, 40000, 80000, 65000],
    'age': [28, 35, 40, 50, 30]
}

df = pd.DataFrame(data)

# Sort by salary
df.sort_values(by='salary', ascending=False)

# Filter: IT department with salary > 60000
df[(df['department'] == 'IT') & (df['salary'] > 60000)]

# Filter using query
df.query("department == 'HR' and age > 30")

# | Function / Method       | Description                         |
# | ----------------------- | ----------------------------------- |
# | `sort_values(by=...)`   | Sort by column(s)                   |
# | `sort_index()`          | Sort by index                       |
# | `df[condition]`         | Basic filtering                     |
# | `.isin([...])`          | Filter by multiple values           |
# | `.between(start, end)`  | Filter by range                     |
# | `.str.contains('text')` | Text-based filter on string columns |
# | `.query(\"expr\")`      | SQL-style filtering                 |

