import numpy as np
# Axis-wise Operations in NumPy 
# a super useful concept for applying functions across rows or columns of arrays.

# What is an Axis?
# In NumPy:
# axis=0 → operates down the rows (i.e., column-wise)
# axis=1 → operates across the columns (i.e., row-wise)

# Axis Visualized
# For this array:
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# axis=0 = ⬇ column-wise (↓ down)
# Acts on: [1, 4], [2, 5], [3, 6]

# axis=1 = ➡ row-wise (→ across)
# Acts on: [1, 2, 3], [4, 5, 6]

#  Examples with axis
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

# Column-wise sum (axis=0)
np.sum(arr, axis=0)  # [5 7 9]

# Row-wise sum (axis=1)
np.sum(arr, axis=1)  # [6 15]

# Column-wise mean
np.mean(arr, axis=0)  # [2.5 3.5 4.5]

# Row-wise max
np.max(arr, axis=1)   # [3 6]

# Standard deviation column-wise
np.std(arr, axis=0)   # [1.5 1.5 1.5]

# When to Use Axis-Wise Operations?
# | Use Case              | Axis     | Explanation                     |
# | --------------------- | -------- | ------------------------------- |
# | Sum per column        | `axis=0` | Combine data from multiple rows |
# | Average per row       | `axis=1` | Average a student's scores      |
# | Normalize column-wise | `axis=0` | Feature scaling in ML           |
# | Row min/max           | `axis=1` | Find best/worst per sample      |

# 1D Arrays
# Axis values are ignored for 1D arrays — there's no direction to apply across:
arr1d = np.array([1, 2, 3])
np.sum(arr1d)  # 6
np.sum(arr1d, axis=0)  # still 6

# | Function       | `axis=None` (default) | `axis=0`        | `axis=1`     |
# | -------------- | --------------------- | --------------- | ------------ |
# | `np.sum(arr)`  | Sum of all elements   | Sum of columns  | Sum of rows  |
# | `np.mean(arr)` | Mean of all elements  | Mean per column | Mean per row |
# | `np.max(arr)`  | Max of all elements   | Max per column  | Max per row  |
# | `np.std(arr)`  | Std dev of all        | Std per column  | Std per row  |

