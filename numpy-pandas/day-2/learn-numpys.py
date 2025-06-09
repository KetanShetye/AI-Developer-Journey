# num py

# np.array()
# np.array() is used to create a NumPy array, the fundamental object in NumPy, similar to Python lists but optimized for performance and multidimensional data.

import numpy as np

a = np.array([1, 2, 3])

# Array Dimensions
# | Dimension   | Description  | Example                              |
# | ----------- | ------------ | ------------------------------------ |
# | 0D (scalar) | Single value | `np.array(42)`                       |
# | 1D          | Vector       | `np.array([1, 2, 3])`                |
# | 2D          | Matrix       | `np.array([[1, 2], [3, 4]])`         |
# | 3D          | Tensor       | `np.array([[[1], [2]], [[3], [4]]])` |

# Data Types (dtype)
# By default, NumPy infers the data type, but you can specify using dtype.
arr = np.array([1, 2, 3], dtype=float)
print(arr.dtype)  # float64
#  Common dtypes: int32, float64, bool, complex, str_

# Type Conversion (Casting)
# You can convert arrays from one dtype to another.
arr = np.array([1.5, 2.3])
int_arr = arr.astype(int)
print(int_arr)  # [1 2]

# Checking Properties
arr = np.array([[1, 2, 3], [4, 5, 6]])

print("Shape:", arr.shape)      # (2, 3)
print("Size:", arr.size)        # 6
print("Dimensions:", arr.ndim)  # 2
print("Data type:", arr.dtype)  # int64 (depends on system)

# Creating Arrays Quickly
# | Function        | Description                       | Example                |
# | --------------- | --------------------------------- | ---------------------- |
# | `np.zeros()`    | All zeros                         | `np.zeros((2,3))`      |
# | `np.ones()`     | All ones                          | `np.ones((2,3))`       |
# | `np.full()`     | All elements with specified value | `np.full((2,2), 7)`    |
# | `np.eye()`      | Identity matrix                   | `np.eye(3)`            |
# | `np.arange()`   | Range array                       | `np.arange(1, 10, 2)`  |
# | `np.linspace()` | Evenly spaced values              | `np.linspace(0, 1, 5)` |
# | `np.empty()`    | Uninitialized array               | `np.empty((2,2))`      |

# Nested Lists → Multidimensional Arrays
nested = [[1, 2], [3, 4]]
arr = np.array(nested)
print(arr)
# Output:
# [[1 2]
#  [3 4]]
# Must have equal-length inner lists; otherwise, it will create a 1D object array.

# Object Arrays (Avoid unless needed)
weird = np.array([1, 'a', True])
print(weird)         # ['1' 'a' 'True']
print(weird.dtype)   # <U5 (unicode string)
# Mixed types get converted to a common type (usually string).
# If shape is inconsistent: creates dtype=object

# Copy vs View
arr = np.array([1, 2, 3])
copy_arr = arr.copy()
view_arr = arr.view()

arr[0] = 99
print(copy_arr)  # [1 2 3]
print(view_arr)  # [99 2 3]
# Copy → New memory block.
# View → Shares memory.

# Performance Difference with Lists
import time

lst = list(range(1000000))
arr = np.array(lst)

start = time.time()
lst2 = [x + 1 for x in lst]
print("List time:", time.time() - start)

start = time.time()
arr2 = arr + 1
print("Array time:", time.time() - start)
# NumPy is much faster due to vectorized operations and C-optimizations.

# Real Use Case
# Convert temperature from Celsius to Fahrenheit:
celsius = np.array([0, 10, 20, 30])
fahrenheit = celsius * 1.8 + 32
print(fahrenheit)

# Array Indexing and Slicing in NumPy
# Understanding how to access elements is key for manipulating data in arrays.

# Basic Indexing (1D Array)
import numpy as np

arr = np.array([10, 20, 30, 40, 50])
print(arr[0])    # 10
print(arr[-1])   # 50 (last element)

# Indexing in 2D Arrays
arr2d = np.array([[1, 2, 3], [4, 5, 6]])

print(arr2d[0][1])   # 2
print(arr2d[1, 2])   # 6 (row 1, col 2)
#  You can use [row][col] or [row, col] syntax.

# Slicing (1D Array)
arr = np.array([10, 20, 30, 40, 50])

print(arr[1:4])     # [20 30 40]
print(arr[:3])      # [10 20 30]
print(arr[::2])     # [10 30 50]
# Syntax: array[start:stop:step]

# Slicing (2D Arrays)
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

print(arr2d[:2, 1:])   # rows 0-1, cols 1-2 → [[2 3], [5 6]]
print(arr2d[::2, ::2]) # every 2nd row/col → [[1 3], [7 9]]

# Boolean Indexing
arr = np.array([10, 15, 20, 25, 30])

print(arr[arr > 20])   # [25 30]

# Fancy Indexing (Using Lists of Indexes)
arr = np.array([10, 20, 30, 40, 50])
print(arr[[0, 2, 4]])  # [10 30 50]

# Indexing with np.where()
arr = np.array([5, 10, 15, 20])
print(np.where(arr > 10))  # (array([2, 3]),)


# Array Math and Broadcasting in NumPy
# This is one of the biggest advantages of NumPy: you can do element-wise operations without loops, thanks to vectorization and broadcasting.

# Element-wise Arithmetic
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)   # [5 7 9]
print(a - b)   # [-3 -3 -3]
print(a * b)   # [4 10 18]
print(b / a)   # [4.0 2.5 2.0]

# Scalar Operations
# You can also perform operations between arrays and scalars:
a = np.array([1, 2, 3])
print(a + 10)   # [11 12 13]
print(a * 2)    # [2 4 6]

# Broadcasting Basics
# Broadcasting automatically expands smaller shapes so operations can happen across arrays of different shapes.
a = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([10, 20, 30])  # 1D array (3,)
print(a + b)

# Output:
# [[11 22 33]
#  [14 25 36]]
# Rules:
# Dimensions are matched from right to left
# If sizes don’t match:
# If one of them is 1, it's broadcasted
# If not, error

# Common Mathematical Functions
arr = np.array([1, 2, 3, 4])

print(np.mean(arr))     # 2.5
print(np.max(arr))      # 4
print(np.min(arr))      # 1
print(np.sum(arr))      # 10
print(np.sqrt(arr))     # [1. 1.41 1.73 2.]
print(np.exp(arr))      # e^x
print(np.log(arr))      # natural log

#  Matrix Operations
a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

print(np.dot(a, b))     # Matrix multiplication
print(a @ b)            # Same as dot()
# Use np.dot() or @ for matrix multiplication
# Use * for element-wise multiplication

# reshape(), flatten(), transpose(), dtype
# These methods are essential when transforming array structure or inspecting types.

# reshape()
# 🔄 Changes the shape of the array without changing its data.
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr.reshape((2, 3))  # 2 rows, 3 columns
print(reshaped)
# Output:
# [[1 2 3]
#  [4 5 6]]
# Must match original number of elements (2*3 = 6 in this case)

# flatten()
# Converts multi-dimensional array into 1D
arr2d = np.array([[1, 2], [3, 4]])
flat = arr2d.flatten()
print(flat)   # [1 2 3 4]
#  Similar: ravel() (returns a view instead of a copy if possible)

# transpose()
# 🔁 Swaps rows and columns in a 2D array (or permutes axes in higher dims)
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

transposed = arr.transpose()
print(transposed)
# Output:
# [[1 4]
#  [2 5]
#  [3 6]]
# Or use shortcut: arr.T

# dtype
# 🧬 Returns or sets data type of array elements.
arr = np.array([1, 2, 3])
print(arr.dtype)       # int64 or int32 depending on system

arr2 = np.array([1, 2, 3], dtype='float32')
print(arr2.dtype)      # float32

# Convert with astype():
arr3 = arr.astype(float)


