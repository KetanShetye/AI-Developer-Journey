# Series and DataFrame Creation

# What is a Series?
# A Series is a one-dimensional labeled array capable of holding any data type (integers, strings, floats, etc.).

# Creating a Series
import pandas as pd

# From a list
s1 = pd.Series([10, 20, 30, 40])

# From a dictionary
s2 = pd.Series({'a': 100, 'b': 200, 'c': 300})

# With custom index
s3 = pd.Series([1, 2, 3], index=['x', 'y', 'z'])

print(s1)
print(s2)
print(s3)

# What is a DataFrame?
# A DataFrame is a two-dimensional labeled data structure with columns that can be of different types (like a spreadsheet or SQL table).

# Creating a DataFrame
# From a dictionary of lists
df1 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Score': [85.0, 90.5, 88.0]
})

# From a list of dictionaries
df2 = pd.DataFrame([
    {'Name': 'David', 'Age': 40},
    {'Name': 'Eva', 'Age': 28, 'Score': 92.5}
])

# From a 2D list
df3 = pd.DataFrame(
    [[1, 2], [3, 4]],
    columns=['Col1', 'Col2']
)

print(df1)
print(df2)
print(df3)


# | Use Case                            | Method                         |
# | ----------------------------------- | ------------------------------ |
# | Create Series from list             | `pd.Series([10, 20, 30])`      |
# | Create Series from dict             | `pd.Series({'a': 1, 'b': 2})`  |
# | Create DataFrame from dict of lists | `pd.DataFrame({...})`          |
# | Create DataFrame from list of dicts | `pd.DataFrame([{...}, {...}])` |
# | Create DataFrame from 2D list       | `pd.DataFrame([[...], [...]])` |
