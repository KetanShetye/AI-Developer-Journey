# Data Inspections
# which is all about understanding the structure, types, and summary of your data right after loading it.

#  Data Inspection in Pandas
# When you read data into a DataFrame, it’s important to quickly inspect it to understand:
# What kind of data it holds (numerical, categorical, missing)
# How many rows and columns
# Summary statistics
# Any missing values

# head() – View Top Rows
# df.head()         # First 5 rows
# df.head(10)       # First 10 rows
#  Use Case: See sample data immediately after loading.

# tail() – View Bottom Rows
# df.tail()         # Last 5 rows
# df.tail(3)        # Last 3 rows
#  Use Case: Check trailing rows, useful for time series data.

#  shape – Rows and Columns
# df.shape          # (rows, columns)
# ✅ Use Case: Know your data size quickly.

# columns – Column Names
# df.columns        # Index object of column names
# list(df.columns)  # Convert to list
# ✅ Use Case: Helps access, rename, or filter columns.

# dtypes – Data Types of Columns
# df.dtypes         # Shows type of each column
# ✅ Use Case: Detect incorrect types (e.g., numbers stored as strings).

# info() – Full DataFrame Summary
# df.info()
# ✅ Use Case: Get memory usage, non-null count, and datatypes.

# describe() – Summary Statistics
# df.describe()         # Numeric columns only
# df.describe(include='all')  # Include all columns
# ✅ Use Case: View mean, std, min, max, count, etc. for quick analysis.

# value_counts() – Frequency Count
# df['column_name'].value_counts()
# ✅ Use Case: Analyze class distribution or categorical features.

# isnull() and sum() – Missing Values
# df.isnull().sum()   # Count of nulls per column
# df.isnull().any()   # True if any nulls in column
# ✅ Use Case: Handle missing data early in the pipeline.

# unique() and nunique() – Unique Values
# df['column'].unique()    # All unique values
# df['column'].nunique()   # Count of unique values
# ✅ Use Case: Great for categorical data exploration.

# | Function         | Purpose                          |
# | ---------------- | -------------------------------- |
# | `head(n)`        | View first *n* rows              |
# | `tail(n)`        | View last *n* rows               |
# | `shape`          | Tuple of (rows, columns)         |
# | `columns`        | Get column names                 |
# | `dtypes`         | Get column data types            |
# | `info()`         | Full structure overview          |
# | `describe()`     | Summary statistics               |
# | `value_counts()` | Count frequency of unique values |
# | `isnull()`       | Check for missing values         |
# | `unique()`       | Return array of unique values    |
# | `nunique()`      | Number of unique values          |

