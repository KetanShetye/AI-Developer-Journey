# Handling Duplicates
# a common and important data cleaning step.
# Duplicates can occur due to data entry errors, merging datasets, or scraping issues. Pandas provides intuitive methods to detect and remove them.

#  Detect Duplicates
# duplicated()
# df.duplicated()
#  Returns: Boolean Series (True if the row is a duplicate of a previous row)
# df[df.duplicated()]

# Parameters of duplicated():
# | Parameter | Description                                                      |
# | --------- | ---------------------------------------------------------------- |
# | `subset`  | Column(s) to check for duplicates                                |
# | `keep`    | `'first'` (default), `'last'`, or `False` to mark all duplicates |

# df.duplicated(subset=['Name'], keep='first')   # Keep first duplicate
# df.duplicated(subset=['Name'], keep=False)     # Mark all duplicates as True

#  Drop Duplicates
# drop_duplicates()
# df.drop_duplicates()
# ✅ Removes duplicated rows. Keeps first by default.

# Parameters of drop_duplicates():
# | Parameter | Description                                |
# | --------- | ------------------------------------------ |
# | `subset`  | Column(s) to check                         |
# | `keep`    | `'first'`, `'last'`, or `False`            |
# | `inplace` | If `True`, modifies the original DataFrame |

# df.drop_duplicates(subset=['Name'])  # Remove duplicate names
# df.drop_duplicates(keep='last')      # Keep last occurrence
# df.drop_duplicates(keep=False)       # Drop all duplicates

#  Count Duplicates
# df.duplicated().sum()

# Example
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob'],
    'Age': [25, 30, 25, 35, 30]
}
df = pd.DataFrame(data)

# Detect duplicates
df.duplicated()

# Drop duplicates based on all columns
df.drop_duplicates()

# Drop based on specific column
df.drop_duplicates(subset=['Name'])

# | Function               | Purpose                                 |
# | ---------------------- | --------------------------------------- |
# | `df.duplicated()`      | Detect duplicate rows                   |
# | `df.drop_duplicates()` | Remove duplicate rows                   |
# | `subset`               | Specify columns to check                |
# | `keep`                 | `'first'`, `'last'`, or `False`         |
# | `inplace=True`         | Apply changes to the original DataFrame |
