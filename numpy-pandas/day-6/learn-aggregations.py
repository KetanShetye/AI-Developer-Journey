# Aggregations in Pandas using 
# essential for summarizing and analyzing data.

# Aggregation
# Aggregation refers to applying summary functions to groups or entire datasets to get meaningful insights, such as totals, averages, and counts.

# Basic Aggregation on Entire DataFrame
# df.sum()
# df.mean()
# df.count()
# df.max()
# df.min()
# 🔸 These apply to numeric columns by default.

# Aggregation on Specific Columns
# df['revenue'].sum()
# df[['sales', 'profit']].mean()

# Aggregation with groupby()
# df.groupby('region')['sales'].sum()
# df.groupby('department')[['salary', 'bonus']].mean()

# Using .agg() for Multiple Aggregations
# df.agg({
#     'sales': ['sum', 'mean'],
#     'profit': ['max', 'min']
# })
# 🔸 This allows column-wise aggregation with different functions.

# Aggregation with Renamed Output Columns
# df.groupby('product').agg(
#     total_sales=('sales', 'sum'),
#     avg_profit=('profit', 'mean'),
#     order_count=('order_id', 'count')
# )
# ✅ This improves readability and usability.

# Using Custom Aggregation Functions
# df.agg({'sales': lambda x: x.max() - x.min()})

# Aggregating with apply() for Custom Logic
# df.groupby('region').apply(lambda x: x['sales'].sum() / x['orders'].sum())

# Aggregating Only Non-Null Values
# All aggregation methods in Pandas ignore NaN values by default:
# df['sales'].sum()  # skips NaN

#  Counting Non-Null vs Total
# df['product'].count()    # non-null values only
# df['product'].size       # total number of rows

# Aggregation in Pivot Tables
# df.pivot_table(values='sales', index='region', aggfunc='sum')
# 🔸 Useful for multi-level aggregations.

import pandas as pd

data = {
    'department': ['IT', 'IT', 'HR', 'HR', 'Finance'],
    'salary': [70000, 65000, 40000, 42000, 80000],
    'bonus': [5000, 6000, 2000, 2500, 7000]
}

df = pd.DataFrame(data)

# Basic aggregations
df.sum()
df['salary'].mean()

# Grouped aggregations
df.groupby('department')['salary'].mean()

# Aggregating multiple metrics
df.groupby('department').agg(
    total_salary=('salary', 'sum'),
    avg_bonus=('bonus', 'mean')
)


# | Function          | Description                   |
# | ----------------- | ----------------------------- |
# | `sum()`           | Sum of values                 |
# | `mean()`          | Average value                 |
# | `count()`         | Count of non-null values      |
# | `max()` / `min()` | Maximum / Minimum value       |
# | `.agg()`          | Combine multiple aggregations |
# | `.apply()`        | Custom aggregation logic      |
# | `pivot_table()`   | Aggregation in pivot format   |
