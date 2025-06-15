# Vectorization over loops
# core concept in NumPy and Pandas that significantly improves performance and code readability.

# Vectorization is the process of performing operations on entire arrays (or series/dataframes) without using explicit loops (like for or while). 
# It is made possible by NumPy's underlying C implementation and Pandas' optimized internals.
# Instead of iterating through elements one by one, vectorized operations apply functions to entire data structures at once.

# Why use Vectorization?
# | Feature           | Vectorized Code       | Loops                  |
# | ----------------- | --------------------- | ---------------------- |
# | Performance       | 🚀 Fast (C-level ops) | 🐢 Slow (Python-level) |
# | Readability       | ✅ Clean & concise     | ❌ Verbose              |
# | Memory Efficiency | ✅ Optimized           | ❌ Overhead             |

# 🧪 Example 1: NumPy – Squaring numbers
# ❌ Using Loop:
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
squared = []
for i in arr:
    squared.append(i**2)
print(squared)
# Output: [1, 4, 9, 16, 25]

# ✅ Vectorized:
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
squared = arr ** 2
print(squared)
# Output: [ 1  4  9 16 25]

# 🧪 Example 2: Pandas – Apply 10% discount to prices
# ❌ Using Loop:
import pandas as pd

df = pd.DataFrame({'price': [100, 200, 300, 400]})
discounted = []
for p in df['price']:
    discounted.append(p * 0.9)
df['discounted'] = discounted
print(df)

# ✅ Vectorized:
import pandas as pd

df = pd.DataFrame({'price': [100, 200, 300, 400]})
df['discounted'] = df['price'] * 0.9
print(df)

# 🧪 Example 3: Conditional Operation with NumPy
# ❌ Loop:
arr = np.array([10, 20, 30, 40])
result = []
for x in arr:
    if x > 20:
        result.append("High")
    else:
        result.append("Low")
print(result)

# ✅ Vectorized with np.where:
arr = np.array([10, 20, 30, 40])
result = np.where(arr > 20, "High", "Low")
print(result)
# Output: ['Low' 'Low' 'High' 'High']

# ✅ Key Vectorized Functions:
# | NumPy Function                                      | Description               |
# | --------------------------------------------------- | ------------------------- |
# | `np.add`, `np.subtract`, `np.multiply`, `np.divide` | Vectorized arithmetic     |
# | `np.where`                                          | Conditional logic         |
# | `np.sum`, `np.mean`, `np.std`                       | Aggregate ops over arrays |
# | `np.dot`, `np.matmul`                               | Linear algebra            |

# | Pandas Operation    | Description                  |
# | ------------------- | ---------------------------- |
# | `df['col'] * 2`     | Multiply entire column       |
# | `df['col'].apply()` | Use custom function (slower) |
# | `df.loc`, `df.iloc` | Indexed operations           |

# 🧠 Pro Tip:
# Avoid using .apply() if a vectorized operation is available — .apply() is just syntactic sugar around loops.