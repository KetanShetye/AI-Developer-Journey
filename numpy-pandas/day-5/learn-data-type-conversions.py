# Data type conversions
# Pandas allows converting the data types (also called dtypes) of Series or DataFrame columns, such as from object to int, float, datetime, or category.
# an essential skill for preparing and optimizing datasets for analysis or modeling.

# Checking Data Types
# df.dtypes       # Shows data types of each column
# df.info()       # Shows data types + null counts + memory usage

# Convert Data Types with astype()
# df['column'] = df['column'].astype('int')     # to integer
# df['column'] = df['column'].astype('float')   # to float
# df['column'] = df['column'].astype('str')     # to string
# df['column'] = df['column'].astype('category')# to category

# ✅ Use Case: Convert object column to int for mathematical operations.

# Convert to Date/Time with pd.to_datetime()
# df['date'] = pd.to_datetime(df['date'])
# ➡️ Automatically infers formats like YYYY-MM-DD, DD/MM/YYYY, etc.
# Extra options:
# pd.to_datetime(df['date'], errors='coerce', format='%d-%m-%Y')

# Convert to Numeric with pd.to_numeric()
# df['col'] = pd.to_numeric(df['col'])
# Optional arguments:
# errors='coerce': invalid parsing results in NaN
# downcast='integer': save memory

# pd.to_numeric(df['col'], errors='coerce', downcast='float')

# Convert to Categorical
# df['gender'] = df['gender'].astype('category')
# ✅ Reduces memory usage for columns with few unique values.

import pandas as pd

data = {
    'Age': ['25', '30', '35'],
    'JoiningDate': ['2021-01-01', '2021-03-15', '2021-06-01'],
    'Gender': ['Male', 'Female', 'Male']
}

df = pd.DataFrame(data)

# Convert Age to int
df['Age'] = df['Age'].astype('int')

# Convert JoiningDate to datetime
df['JoiningDate'] = pd.to_datetime(df['JoiningDate'])

# Convert Gender to category
df['Gender'] = df['Gender'].astype('category')


# | Function             | Purpose                                |
# | -------------------- | -------------------------------------- |
# | `df.dtypes`          | Check column data types                |
# | `df.astype()`        | Convert between int, float, str, etc.  |
# | `pd.to_datetime()`   | Convert to datetime                    |
# | `pd.to_numeric()`    | Convert to int/float safely            |
# | `astype('category')` | Optimize memory for limited categories |
