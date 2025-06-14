# Indexing And Slicing
# Pandas gives us powerful ways to access rows, columns, and sub-sections of data using:
# .loc – label-based indexing
# .iloc – integer position-based indexing
# Basic slicing techniques (like df[columns], df[rows])
# Conditional indexing

# Selecting Columns
# df['col_name']         # Single column (returns Series)
# df[['col1', 'col2']]   # Multiple columns (returns DataFrame)

# Selecting Rows by Index
# df[5:10]               # Row slice from position 5 to 9
# df[:3]                 # First 3 rows

# .loc[] – Label-Based Indexing
# df.loc[row_label, column_label]

# Examples:
# df.loc[0]                          # Row with index label 0
# df.loc[0, 'Name']                 # Value at row 0, column 'Name'
# df.loc[:, ['Name', 'Score']]     # All rows, specific columns
# df.loc[2:4, 'Name':'Score']      # Rows 2 to 4, columns 'Name' to 'Score'

# 🔸 Works with row and column labels
# 🔸 Includes both endpoints when slicing

# .iloc[] – Position-Based Indexing
# df.iloc[row_index, column_index]

# df.iloc[0]                # First row
# df.iloc[2, 1]             # Element at 3rd row, 2nd column
# df.iloc[:, 0:2]           # All rows, first two columns
# df.iloc[1:4, 0:2]         # Rows 1 to 3, columns 0 and 1

# 🔸 Uses integer indices only
# 🔸 Right endpoint excluded in slicing

# Conditional Indexing (Boolean Masking)
# df[df['Age'] > 30]                         # Filter rows where Age > 30
# df[(df['Age'] > 25) & (df['Score'] > 80)] # Multiple conditions
# df[df['Name'].isin(['Alice', 'Bob'])]     # Filter by values in list

# Set Values Using .loc and .iloc
# df.loc[0, 'Name'] = 'John'
# df.iloc[1, 2] = 99.5

# Reverse Indexing
# df.iloc[::-1]          # Reverse rows
# df.iloc[:, ::-1]       # Reverse columns

# | Method              | Type             | Example                           |
# | ------------------- | ---------------- | --------------------------------- |
# | `df[col]`           | Column selection | `df['Age']`                       |
# | `df.loc[]`          | Label-based      | `df.loc[1, 'Score']`              |
# | `df.iloc[]`         | Position-based   | `df.iloc[1, 2]`                   |
# | `df[:]`             | Row slicing      | `df[2:5]`                         |
# | Boolean Indexing    | Condition-based  | `df[df['Age'] > 30]`              |
# | `isin()`            | Membership check | `df[df['Name'].isin(['A', 'B'])]` |
# | `df.loc[cond, col]` | Cond. + col      | `df.loc[df['Age'] > 30, 'Score']` |
