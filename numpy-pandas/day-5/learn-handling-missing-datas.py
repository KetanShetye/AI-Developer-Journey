# Handling Missing Data
#  a core concept in data cleaning and preprocessing.

# Handling Missing Data in Pandas
# Missing data can appear as:
# NaN (Not a Number)
# None (null in Python)
# Empty strings (in some datasets)
# Pandas provides several powerful tools for detecting, removing, or filling missing values.

# Detect Missing Values
# isna() / isnull()
# Returns a DataFrame of boolean values where True indicates missing.
# df.isna() 
# df.isnull()  # same as isna()

# notna() / notnull()
# Returns True for non-missing values.
# df.notna()
# df.notnull()

#  Use Case:
# df[df['Age'].isna()]  # Rows where 'Age' is missing

# Remove Missing Values
# dropna()
# df.dropna()            # Drop rows with any NaNs
# df.dropna(axis=1)      # Drop columns with any NaNs
# df.dropna(how='all')   # Drop rows where *all* elements are NaN
# df.dropna(thresh=2)    # Keep rows with at least 2 non-NaNs
# df.dropna(subset=['Age', 'Salary'])  # Only consider these columns

# Fill Missing Values
# fillna()
# df.fillna(0)                         # Replace NaN with 0
# df.fillna(method='ffill')           # Forward fill
# df.fillna(method='bfill')           # Backward fill
# df.fillna(value={'Age': 25, 'Salary': 0})  # Fill by column


# Custom logic:
# df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

# Replace Values (alternative to fillna for non-NaN)
# df.replace('?', np.nan)     # Replace placeholder with NaN

# Interpolate Missing Values
# df.interpolate(method='linear')
# Useful for time series or numerical sequences.

import pandas as pd
import numpy as np

data = {
    'Name': ['Alice', 'Bob', 'Charlie', None],
    'Age': [25, np.nan, 30, 22],
    'Salary': [50000, 60000, None, None]
}
df = pd.DataFrame(data)

df.isna()
df.dropna()
df.fillna({'Age': df['Age'].mean(), 'Salary': 0})


# | Function                | Purpose                                |
# | ----------------------- | -------------------------------------- |
# | `isna()` / `isnull()`   | Detect missing values (NaN, None)      |
# | `notna()` / `notnull()` | Detect non-missing values              |
# | `dropna()`              | Remove rows/columns with missing data  |
# | `fillna()`              | Fill missing data with values or logic |
# | `replace()`             | Replace specific values (e.g., '?')    |
# | `interpolate()`         | Estimate missing values numerically    |
