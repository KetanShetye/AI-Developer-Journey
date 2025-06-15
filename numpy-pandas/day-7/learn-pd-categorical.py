# pd.Categorical
# it is key to optimizing memory and enabling efficient, ordered categorical operations in Pandas.

# ✅ Working with Categorical Data using pd.Categorical
# 🧩 What is Categorical Data?
# Categorical data is data that takes on a limited, fixed number of values, such as:
# Gender: ["Male", "Female"]
# Education: ["High School", "Bachelor", "Master", "PhD"]
# Grades: ["A", "B", "C", "D", "F"]
# These values are not numeric, but they can be ordered or unordered categories.

# 🛠 Why Use pd.Categorical?
# Saves memory compared to object dtype
# Allows ordering
# Enables faster comparisons and grouping

# 🧪 Example 1: Convert to Categorical
# import pandas as pd
# df = pd.DataFrame({'grade': ['A', 'B', 'A', 'C', 'B', 'A']})
# df['grade'] = pd.Categorical(df['grade'])
# print(df['grade'].dtype)  # category

# 🧪 Example 2: Define Ordered Categories
# grades = pd.Categorical(
#     ['A', 'B', 'C', 'A'],
#     categories=['A', 'B', 'C', 'D', 'F'],
#     ordered=True
# )
# Now you can do:
# grades.min()  # 'A'
# grades.max()  # 'C'
# grades > 'B'  # Boolean mask

# 🧪 Example 3: Use with DataFrames
# df = pd.DataFrame({
#     'education': ['PhD', 'Bachelor', 'Master', 'High School'],
# })

# df['education'] = pd.Categorical(
#     df['education'],
#     categories=['High School', 'Bachelor', 'Master', 'PhD'],
#     ordered=True
# )

# Now you can sort or compare easily:
# df.sort_values('education')

# 🧠 Best Practices
# | Action                       | Example                                                     |
# | ---------------------------- | ----------------------------------------------------------- |
# | Convert string to category   | `df['col'] = df['col'].astype('category')`                  |
# | Define custom order          | `pd.Categorical([...], categories=[...], ordered=True)`     |
# | Sort based on category order | `df.sort_values('col')`                                     |
# | Filter using comparisons     | `df[df['col'] > 'B']` (only if ordered categories are used) |

# 📉 Memory Usage Comparison
# df['col'].memory_usage(deep=True)  # object → high
# df['col'].astype('category').memory_usage(deep=True)  # category → lower


