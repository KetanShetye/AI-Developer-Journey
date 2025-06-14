# Boolean Indexing & Filtering in NumPy

# Boolean Indexing
# Boolean indexing allows you to select elements from an array based on conditions.
# You create a boolean mask (True/False array) and use it to extract elements.

# ✅ Basic Example
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Create boolean condition
mask = arr > 30   # [False False False  True  True]

# Filter elements using mask
filtered = arr[mask]  # [40 50]

# Combine in one step
arr[arr > 30]  # [40 50]

#  Filtering with Conditions
# | Condition               | Meaning       | Example                        |                    |                |
# | ----------------------- | ------------- | ------------------------------ | ------------------ | -------------- |
# | `arr > x`               | Greater than  | `arr[arr > 30]`                |                    |                |
# | `arr < x`               | Less than     | `arr[arr < 25]`                |                    |                |
# | `arr == x`              | Equal to      | `arr[arr == 20]`               |                    |                |
# | `arr != x`              | Not equal     | `arr[arr != 10]`               |                    |                |
# | `(arr > x) & (arr < y)` | AND condition | `arr[(arr > 10) & (arr < 50)]` |                    |                |
# | \`(arr == x)            | (arr == y)\`  | OR condition                   | \`arr\[(arr == 10) | (arr == 50)]\` |

# NOTE :- Use &, |, ~ (not and / or / not) and wrap conditions in parentheses.

# Filtering 2D Arrays
mat = np.array([
    [5, 10, 15],
    [20, 25, 30]
])

# Get all elements > 15
mat[mat > 15]  # [20 25 30]

# Filter specific row
mat[1][mat[1] > 20]  # [25 30]

# Boolean Mask from Another Array
data = np.array([100, 200, 300, 400])
mask = np.array([True, False, True, False])
data[mask]  # [100 300]

# | Use Case             | Example                        |
# | -------------------- | ------------------------------ |
# | Filter ages above 18 | `ages[ages > 18]`              |
# | Remove NaNs or zeros | `arr[arr != 0]`                |
# | Replace values       | `arr[arr > 10] = 0`            |
# | Conditional logic    | `arr[(arr > 10) & (arr < 50)]` |

# 🚫 Modifying Values Conditionally
arr = np.array([1, 2, 3, 4, 5])
arr[arr > 3] = 100
print(arr)  # [  1   2   3 100 100]

