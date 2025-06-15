# MultiIndex (Hierarchical indexing) in Pandas for complex datasets
# also called Hierarchical Indexing
# powerful feature in Pandas that lets you work with higher-dimensional data in a 2D DataFrame.

# 📌 What is a MultiIndex?
# A MultiIndex allows multiple (two or more) index levels on rows or columns, enabling you to organize complex datasets like time series, grouped data, pivoted tables, or panel data.

# 🛠 Creating a MultiIndex
# 🔹 From a list of tuples:
arrays = [
    ['Math', 'Math', 'Science', 'Science'],
    ['Grade 9', 'Grade 10', 'Grade 9', 'Grade 10']
]

# index = pd.MultiIndex.from_arrays(arrays, names=('Subject', 'Grade'))
# df = pd.DataFrame([[85, 90], [88, 92], [79, 83], [81, 87]], index=index, columns=['Term 1', 'Term 2'])

# 📊 Example Output
#                   Term 1  Term 2
# Subject Grade                  
# Math    Grade 9       85      90
#         Grade 10      88      92
# Science Grade 9       79      83
#         Grade 10      81      87

# 🔧 Accessing Data in MultiIndex
# 🔹 Access using .loc[]
# df.loc[('Math', 'Grade 10')]

# 🔹 Access a specific cell:
# df.loc[('Science', 'Grade 9'), 'Term 2']

# 🔄 Swapping & Sorting Levels
# df = df.swaplevel()            # Swap level 0 and 1
# df = df.sort_index()           # Sort by index

# 🔍 Index Methods
# | Operation             | Code                             |
# | --------------------- | -------------------------------- |
# | Set MultiIndex        | `df.set_index(['col1', 'col2'])` |
# | Reset to single index | `df.reset_index()`               |
# | Check index levels    | `df.index.names`                 |
# | Access level values   | `df.index.get_level_values(0)`   |

# 🧮 Aggregation with MultiIndex
# df.groupby(['Subject', 'Grade']).mean()
# Or, if already a MultiIndex:
# df.groupby(level='Subject').mean()

# 📁 Use Cases
# Time series with multiple dimensions (e.g., Date + Stock)
# Panel data (e.g., Country + Year)
# Pivot tables
# Grouped aggregations (multi-level groupby)

# 🧠 Best Practices
# | Tip                         | Why it matters        |
# | --------------------------- | --------------------- |
# | Use named levels (`names=`) | Improves clarity      |
# | Always sort after swap      | Avoids slicing errors |
# | Reset index for flat output | Easier export/viewing |




