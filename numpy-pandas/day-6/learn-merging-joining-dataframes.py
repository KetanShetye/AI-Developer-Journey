# Merging & Joining DataFrames in Pandas 
# one of the most powerful data manipulation features. 
# It allows you to combine multiple DataFrames similar to SQL joins.

# merge() — SQL-Style Joins
# pd.merge(df1, df2, on='key')

# 🔸 Join Types:
# pd.merge(df1, df2, on='key', how='inner')     # default
# pd.merge(df1, df2, on='key', how='left')      # keep all from df1
# pd.merge(df1, df2, on='key', how='right')     # keep all from df2
# pd.merge(df1, df2, on='key', how='outer')     # full join

# 🔸 Merge on Multiple Keys:
# pd.merge(df1, df2, on=['key1', 'key2'], how='inner')

# 🔸 Merge with Different Column Names:
# pd.merge(df1, df2, left_on='id1', right_on='id2')

# 🔸 Avoid Duplicate Column Names:
# pd.merge(df1, df2, on='key', suffixes=('_left', '_right'))

# join() — Join by Index
# df1.join(df2)

# 🔸 Works when df2's index aligns with df1:
# df1.join(df2, how='inner')
# df1.join(df2, how='outer')

# 🔸 Join on Column (by setting index first):
# df1.set_index('id').join(df2.set_index('id'))

# concat() — Stack DataFrames
# 🔸 Row-wise (Vertical):
# pd.concat([df1, df2], axis=0)

# 🔸 Column-wise (Horizontal):
# pd.concat([df1, df2], axis=1)

# 🔸 With Ignore Index:
# pd.concat([df1, df2], ignore_index=True)

# combine_first() — Fill Missing Values from Another DataFrame
# df1.combine_first(df2)
# ✅ Useful for filling NaN values with fallback DataFrame.

# Append (Deprecated for concat)
# df1.append(df2, ignore_index=True)  # deprecated
# ⚠️ Use pd.concat() instead of .append() in latest versions.

import pandas as pd

employees = pd.DataFrame({
    'emp_id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie']
})

salaries = pd.DataFrame({
    'emp_id': [1, 2, 4],
    'salary': [70000, 80000, 50000]
})

# Inner join
pd.merge(employees, salaries, on='emp_id', how='inner')

# Left join
pd.merge(employees, salaries, on='emp_id', how='left')

# Outer join
pd.merge(employees, salaries, on='emp_id', how='outer')

# | Method            | Purpose                                  | Key Parameters                     |
# | ----------------- | ---------------------------------------- | ---------------------------------- |
# | `merge()`         | SQL-style joins (on keys)                | `on`, `how`, `left_on`, `right_on` |
# | `join()`          | Join on index or key                     | `how`, `on`, `lsuffix`, `rsuffix`  |
# | `concat()`        | Concatenate along rows/columns           | `axis`, `ignore_index`             |
# | `combine_first()` | Fill missing data from another DataFrame | —                                  |
