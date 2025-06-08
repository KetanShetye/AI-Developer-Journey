import numpy as np
import pandas as pd

print("NumPy version:", np.__version__)
print("Pandas version:", pd.__version__)

# NumPy
# NumPy (Numerical Python) is a Python library used for:
# Efficient numerical operations on large arrays and matrices
# Performing mathematical, logical, shape manipulation, and Fourier transforms
# Serving as the base for libraries like Pandas, Scikit-learn, and more

#  Key Features:
# Multidimensional array object: ndarray
# Fast operations on arrays (element-wise, linear algebra, statistics)
# Broadcasting support
# Integration with C/C++

# eg:- 
import numpy as np

# Create a 1D array
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)

# Get basic properties
print("Shape:", arr.shape)
print("Data Type:", arr.dtype)

# Perform operations
print("Array + 10:", arr + 10)
print("Mean:", np.mean(arr))

# NumPy 2D Arrays & Basic Operations
# Create a 2D Array (Matrix)
import numpy as np

matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

print("Matrix:\n", matrix)
print("Shape:", matrix.shape)
print("Dimensions:", matrix.ndim)
print("Data Type:", matrix.dtype)

# Useful Operations
# Element-wise operations
print("Matrix + 10:\n", matrix + 10)

# Matrix transposition
print("Transpose:\n", matrix.T)

# Sum along rows and columns
print("Sum of all elements:", np.sum(matrix))
print("Sum along columns:", np.sum(matrix, axis=0))
print("Sum along rows:", np.sum(matrix, axis=1))

#  Indexing & Slicing
# Access a specific element
print("Element at row 1, col 2:", matrix[0, 1])  # Output: 2

# Access a full row
print("Second row:", matrix[1])

# Access a full column
print("Third column:", matrix[:, 2])

# Pandas 
# Pandas (Python Data Analysis Library) is a Python library used for:

# Data analysis and manipulation

# Handling tabular data (like Excel or SQL tables)

# Reading/writing data from CSV, Excel, SQL, JSON, etc.

# Cleaning, filtering, aggregating, and transforming data easily

# 🔑 Key Features:
# Powerful DataFrame and Series objects

# Easy data selection, filtering, and slicing

# Built-in support for grouping, aggregations, joins, pivoting

# Fast I/O support: read_csv(), to_csv(), read_excel(), etc.

# Built on top of NumPy, integrates well with it

# eg:-
import pandas as pd

# Create a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['Mumbai', 'Delhi', 'Bangalore']
}

df = pd.DataFrame(data)

# View the DataFrame
print("DataFrame:\n", df)

# Get basic info
print("\nShape:", df.shape)
print("Columns:", df.columns)
print("Data Types:\n", df.dtypes)

# Select a column
print("\nNames:\n", df['Name'])

# Filter rows
print("\nPeople older than 28:\n", df[df['Age'] > 28])

# Describe numeric columns
print("\nSummary Stats:\n", df.describe())

# Data Input/Output Examples
# Read CSV
df = pd.read_csv("data.csv")

# Write CSV
df.to_csv("output.csv", index=False)

# when to use NumPy vs Pandas
# | Feature / Use Case              | **NumPy**                                        | **Pandas**                                             |
# | ------------------------------- | ------------------------------------------------ | ------------------------------------------------------ |
# | **Primary Purpose**             | Numerical computations on arrays and matrices    | Data analysis and manipulation of tabular data         |
# | **Data Structure**              | `ndarray` (multi-dimensional array)              | `DataFrame`, `Series` (labeled data structures)        |
# | **Best For**                    | Scientific computing, linear algebra, image data | Tabular data like CSVs, Excel files, databases         |
# | **Indexing**                    | Integer-based indexing                           | Label-based + integer-based indexing                   |
# | **Missing Data Handling**       | Limited support                                  | Built-in handling (e.g., `NaN`, `fillna`, `dropna`)    |
# | **File I/O (CSV, Excel, etc.)** | Not supported directly                           | Built-in functions like `read_csv()`, `read_excel()`   |
# | **Group By, Pivot, Merge**      | Manual implementation needed                     | Built-in and very easy to use                          |
# | **Performance**                 | Faster for large numerical operations            | Slower than NumPy but more powerful for data wrangling |
# | **Dependencies**                | Lightweight, depends on C/C++                    | Built on top of NumPy                                  |
# | **Use Case Example**            | Scientific simulations, image processing         | Data cleaning, analysis, business intelligence         |



# ✅ Use NumPy when you’re dealing with raw numerical data and need high-speed computation.
# ✅ Use Pandas when working with structured data (rows & columns), especially for data analysis, filtering, and preprocessing.
