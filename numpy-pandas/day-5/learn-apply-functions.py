# Applying Functions with .apply() in Pandas
# one of the most powerful and flexible tools in data manipulation.

# .apply() in Pandas
# The .apply() method lets you apply custom or built-in functions to each element, row, or column of a DataFrame or Series.

# Applying on a Series
# Applies a function element-wise on a single column (Series):
# df['col'].apply(func) 
# df['price_with_tax'] = df['price'].apply(lambda x: x * 1.18)

# Applying on a DataFrame (Row-wise or Column-wise)
# df.apply(func, axis=0)  # column-wise (default)
# df.apply(func, axis=1)  # row-wise

# Example (Row-wise total):
# df['total'] = df.apply(lambda row: row['math'] + row['science'], axis=1)

# Using Built-in Functions
# df['length'] = df['name'].apply(len)
# df['square'] = df['num'].apply(pow, args=(2,))  # num^2

# Applying Custom Functions
# def age_group(age):
#     if age < 18:
#         return 'Minor'
#     elif age < 60:
#         return 'Adult'
#     else:
#         return 'Senior'
# df['group'] = df['age'].apply(age_group)
# Using .apply() with lambda and Conditions

# df['discount'] = df['price'].apply(lambda x: 0.1 if x > 100 else 0.05)


# Multiple Conditions in Row-wise .apply()
# def grade(row):
#     if row['math'] >= 90 and row['science'] >= 90:
#         return 'A+'
#     else:
#         return 'B'

# df['grade'] = df.apply(grade, axis=1)

# When Not to Use .apply()
# .apply() is not vectorized, so it’s slower than direct operations.
# Prefer np.where(), vectorized .map() or .str/.dt accessors for performance.

import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'math': [85, 92, 78],
    'science': [90, 88, 95],
    'price': [120, 85, 100]
}
df = pd.DataFrame(data)

# 1. Apply lambda to compute tax
df['price_with_tax'] = df['price'].apply(lambda x: x * 1.18)

# 2. Apply custom row-wise function to get grade
def get_grade(row):
    return 'A' if row['math'] > 90 else 'B'
df['grade'] = df.apply(get_grade, axis=1)

# | Use Case                       | Example                       |
# | ------------------------------ | ----------------------------- |
# | Element-wise on Series         | `df['col'].apply(func)`       |
# | Row-wise or Column-wise        | `df.apply(func, axis=1 or 0)` |
# | With `lambda`                  | `apply(lambda x: ...)`        |
# | With custom function           | `apply(custom_func)`          |
# | With arguments                 | `apply(func, args=(...))`     |
# | Avoid when performance matters | Use vectorized ops instead    |

