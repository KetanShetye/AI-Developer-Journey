# Grouping Data in Pandas using groupby()
# one of the most essential tools for aggregation and data analysis.

#  What is groupby()?
# The groupby() function in Pandas is used to split the data into groups based on some criteria, apply a function, and combine the results — known as the Split-Apply-Combine strategy.

# df.groupby('column_name')

# Simple GroupBy with Aggregation

# df.groupby('category')['value'].sum()
# df.groupby('department')['salary'].mean()
# df.groupby('team').count()

# Multiple Aggregations on Same Column
# df.groupby('city')['sales'].agg(['sum', 'mean', 'max'])

# Grouping by Multiple Columns
# df.groupby(['region', 'product'])['sales'].sum()

# Using .agg() with Custom Function Names
# df.groupby('dept').agg(
#     total_sales=('sales', 'sum'),
#     avg_salary=('salary', 'mean'),
# )

# Iterating Over Groups
# grouped = df.groupby('region')
# for name, group in grouped:
#     print(f"Group: {name}")
#     print(group)

# Filtering Groups
# Use .filter() to keep groups based on a condition:
# df.groupby('category').filter(lambda x: x['value'].sum() > 1000)

# Transforming Groups (element-wise)
# Use .transform() to return a Series of same length as original:
# df['normalized'] = df.groupby('category')['sales'].transform(lambda x: x / x.sum())

# Apply on Groups (custom DataFrame function)
# def top_n(df):
#     return df.sort_values(by='sales', ascending=False).head(2)

# df.groupby('category').apply(top_n)

# Grouping with .resample() for Time Series
# df.resample('M', on='date')['value'].sum()  # Monthly sum

import pandas as pd

data = {
    'department': ['IT', 'HR', 'IT', 'Finance', 'HR', 'Finance'],
    'employee': ['A', 'B', 'C', 'D', 'E', 'F'],
    'salary': [70000, 40000, 65000, 80000, 42000, 85000]
}

df = pd.DataFrame(data)

# Group by department and calculate average salary
df.groupby('department')['salary'].mean()

# Add multiple metrics
df.groupby('department').agg(
    avg_salary=('salary', 'mean'),
    max_salary=('salary', 'max')
)


# | Function / Method                       | Purpose                                 |
# | --------------------------------------- | --------------------------------------- |
# | `groupby('col')`                        | Groups data by column                   |
# | `.agg(['sum', 'mean'])`                 | Multiple aggregations                   |
# | `.agg({'col1': 'sum', 'col2': 'mean'})` | Different aggregations per column       |
# | `.transform()`                          | Element-wise operations within groups   |
# | `.filter(lambda x: ...)`                | Remove/keep groups based on a condition |
# | `.apply(custom_function)`               | Custom logic per group                  |
# | `.resample()`                           | Time-based grouping                     |
