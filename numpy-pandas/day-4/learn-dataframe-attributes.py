# DataFrame Attributes in Pandas
# Attributes are properties (no parentheses) that give info about the DataFrame like column names, data types, index, and dimensions.
# 💡 These are not methods, so you don't use () when calling them.

# df.columns – Column Names
# df.columns
# ✅ Returns: Index of column names
# ✅ Use Case: Helpful for accessing, filtering, renaming columns.

# df.index – Row Index Labels
# ✅ Returns: Index object (e.g., RangeIndex(start=0, stop=100, step=1))
# ✅ Use Case: Useful for resetting or setting custom indexes.

# df.dtypes – Data Types of Columns
# ✅ Returns: Data type of each column (e.g., int64, object, float64)
# ✅ Use Case: Identifying wrong types and casting data.

# df.shape – Dimensions (rows, columns)
# ✅ Returns: Tuple of (number_of_rows, number_of_columns)
# ✅ Use Case: Used for getting the size of the data quickly.

# df.size – Total Elements
# ✅ Returns: Total number of cells (rows × columns)
# ✅ Use Case: Quick way to know how much data is stored.

# df.ndim – Number of Dimensions
# ✅ Returns: 2 for DataFrames (always)
# ✅ Use Case: Confirm the dimensionality of the data.

# df.values – Numpy Array of Data
# ✅ Returns: A 2D NumPy array of the data (without column/index labels)
# ✅ Use Case: Useful when passing to ML models or numerical ops.

# df.axes – List of Row and Column Indexes
# ✅ Returns: [df.index, df.columns]
# ✅ Use Case: Gives an overview of both axes.

# df.T – Transpose the DataFrame
# ✅ Returns: Transposed DataFrame
# ✅ Use Case: Flip rows ↔️ columns, useful for reports or analytics.

#  df.empty – Check if DataFrame is Empty
# ✅ Returns: True if DataFrame has 0 rows or 0 columns
# ✅ Use Case: Useful in condition checks before processing.

# | Attribute           | Description                             |
# | ------------------- | --------------------------------------- |
# | `df.memory_usage()` | Memory used by each column              |
# | `df.nbytes`         | Total bytes consumed by the DataFrame   |
# | `df.style`          | Used for rendering formatting (Jupyter) |
# | `df.at`, `df.iat`   | Fast access to single elements          |


# | Attribute    | Description                              |
# | ------------ | ---------------------------------------- |
# | `df.columns` | List of column names                     |
# | `df.index`   | Row index (e.g., RangeIndex)             |
# | `df.dtypes`  | Data types of each column                |
# | `df.shape`   | Tuple of (rows, columns)                 |
# | `df.size`    | Total number of elements                 |
# | `df.ndim`    | Number of dimensions                     |
# | `df.values`  | Data as NumPy array                      |
# | `df.axes`    | List of index and columns                |
# | `df.T`       | Transposed DataFrame                     |
# | `df.empty`   | Boolean indicating if DataFrame is empty |
