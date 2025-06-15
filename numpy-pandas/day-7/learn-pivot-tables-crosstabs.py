# 📊 Pivot Tables and Crosstabs in Pandas
# two powerful tools for summarizing and reshaping data
# These are essential for data summarization, especially in reporting, analytics, and dashboards.

# 🔁 pivot_table() – Flexible Grouping & Aggregation
# 🔹 Syntax:
# pd.pivot_table(
#     data,
#     values=None,
#     index=None,
#     columns=None,
#     aggfunc='mean',
#     fill_value=None,
#     margins=False
# )
# ✅ Example:
# df = pd.DataFrame({
#     'Department': ['Sales', 'Sales', 'HR', 'HR'],
#     'Gender': ['Male', 'Female', 'Male', 'Female'],
#     'Salary': [50000, 52000, 48000, 47000]
# })

# pd.pivot_table(df, values='Salary', index='Department', columns='Gender', aggfunc='mean')
# Output:
# Gender      Female     Male
# Department                  
# HR           47000     48000
# Sales        52000     50000

# 🧠 Key Options
# | Parameter    | Description                            |
# | ------------ | -------------------------------------- |
# | `index`      | Rows of the output                     |
# | `columns`    | Columns of the output                  |
# | `values`     | Data to aggregate                      |
# | `aggfunc`    | Aggregation function (mean, sum, etc.) |
# | `fill_value` | Fill missing values                    |
# | `margins`    | Add totals (True/False)                |

# 🔁 pd.crosstab() – Frequency Tables (Counts)
# 🔹 Syntax:
# pd.crosstab(index, columns, values=None, aggfunc=None, normalize=False)
# ✅ Example:
# pd.crosstab(df['Department'], df['Gender'])
# Output:
# Gender      Female  Male
# Department              
# HR               1     1
# Sales            1     1

# ✅ Crosstab with Aggregation:
# pd.crosstab(df['Department'], df['Gender'], values=df['Salary'], aggfunc='mean')

# 🧠 Normalize for percentages:
# pd.crosstab(df['Department'], df['Gender'], normalize='index')

# 🧠 When to Use What?
# | Feature               | Use Case Example                               |
# | --------------------- | ---------------------------------------------- |
# | `pivot_table()`       | Flexible aggregation by multiple dimensions    |
# | `pd.crosstab()`       | Quick frequency/count table (like Excel Pivot) |
# | Normalize in crosstab | For proportions/percentages by row/column      |
