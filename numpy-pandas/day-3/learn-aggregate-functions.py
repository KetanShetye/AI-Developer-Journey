# Aggregate Functions in NumPy
# essential for performing summary statistics on arrays.
# Aggregate functions compute a single result from an array or along an axis (e.g., row-wise or column-wise).

# | Function          | Description                                    |
# | ----------------- | ---------------------------------------------- |
# | `np.sum()`        | Sum of all elements                            |
# | `np.mean()`       | Arithmetic mean (average)                      |
# | `np.std()`        | Standard deviation                             |
# | `np.var()`        | Variance                                       |
# | `np.min()`        | Minimum value                                  |
# | `np.max()`        | Maximum value                                  |
# | `np.median()`     | Median value                                   |
# | `np.prod()`       | Product of all elements                        |
# | `np.cumsum()`     | Cumulative sum                                 |
# | `np.cumprod()`    | Cumulative product                             |
# | `np.ptp()`        | Range of values (max - min)                    |
# | `np.percentile()` | N-th percentile                                |
# | `np.quantile()`   | Quantile (like percentile but in \[0,1] scale) |


import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(np.sum(arr))        # 21
print(np.mean(arr))       # 3.5
print(np.std(arr))        # 1.7078
print(np.var(arr))        # 2.9166
print(np.min(arr))        # 1
print(np.max(arr))        # 6
print(np.median(arr))     # 3.5
print(np.prod(arr))       # 720
print(np.cumsum(arr))     # [ 1  3  6 10 15 21]
print(np.cumprod(arr))    # [  1   2   6  24 120 720]
print(np.ptp(arr))        # 5 (max - min)
print(np.percentile(arr, 50))  # 3.5 (50th percentile)
print(np.quantile(arr, 0.75))  # 4.25 (75th quantile)

#  Axis-Wise Operations
# Most of these functions accept an axis argument:
# Sum across rows (axis=1)
np.sum(arr, axis=1)  # [ 6 15 ]

# Mean across columns (axis=0)
np.mean(arr, axis=0)  # [2.5 3.5 4.5]

# | Axis     | Description              |
# | -------- | ------------------------ |
# | `axis=0` | Operates **column-wise** |
# | `axis=1` | Operates **row-wise**    |

# | Function          | Use Case                           |
# | ----------------- | ---------------------------------- |
# | `sum`             | Total sales, scores                |
# | `mean`            | Average grade or reading           |
# | `std`, `var`      | Data spread or variability         |
# | `min`, `max`      | Get bounds for normalization       |
# | `percentile`      | Find salary brackets, percentiles  |
# | `prod`, `cumprod` | Multiplicative factors like growth |
