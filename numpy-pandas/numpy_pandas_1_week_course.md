# NumPy and Pandas in Python - 7-Day Study Plan

This 7-Day Study Plan is designed for Python developers who want to quickly learn NumPy and Pandas for data manipulation, analysis, and computation.


---

## 📅 Day 1: Introduction & Setup
- Install Python, pip, Jupyter Notebook / VS Code
- Install NumPy and Pandas: `pip install numpy pandas`
- What is NumPy?
- What is Pandas?
- When to use NumPy vs Pandas?

## 🔢 Day 2: NumPy Basics
- NumPy arrays: `np.array()`
- Array types, shapes, and dimensions
- Array indexing and slicing
- Array math and broadcasting
- Useful methods: `reshape`, `flatten`, `transpose`, `dtype`

## 🧮 Day 3: NumPy Advanced
- Random module: `np.random`
- Aggregate functions: `sum`, `mean`, `std`, `var`, etc.
- Axis-wise operations
- Boolean indexing and filtering
- Linear algebra: dot, inverse, det, eig, etc.
- NumPy vs Python lists (performance comparison)

## 🧾 Day 4: Pandas Basics
- Series and DataFrame creation
- Reading data
- Data inspection
- Indexing and slicing
- DataFrame attributes

## 🧹 Day 5: Data Cleaning with Pandas
- Handling missing data
- Duplicates
- Data type conversions
- String operations with `.str`
- Applying functions with `.apply()`

## 🔁 Day 6: Grouping, Merging, Aggregation
- Grouping data: `groupby()`
- Aggregations: `sum()`, `mean()`, `count()`
- Sorting and filtering data
- Merging & joining DataFrames: `merge()`, `join()`, `concat()`

## 🛠 Day 7: Tips & Best Practices
- Vectorization over loops
- Use `.copy()` to avoid SettingWithCopyWarning
- Profiling performance with `%timeit`
- Visualizing data using `matplotlib` and `seaborn` (optional)

---

## 🛠 Bonus: Tips & Best Practices
- Vectorization over loops
- Use .copy() to avoid SettingWithCopyWarning
- Profiling performance with %timeit
- Visualizing data using matplotlib and seaborn
- Plotting Cheat Sheet: Matplotlib, Seaborn, Pandas
- Memory optimization in Pandas (e.g., using astype to reduce memory usage)
- Chained indexing vs. loc/iloc – avoid chained indexing for reliability
- Working with categorical data using pd.Categorical
- Datetime handling in Pandas using pd.to_datetime, .dt accessor
- MultiIndex (Hierarchical indexing) in Pandas for complex datasets
- Pivot tables and crosstabs using pivot_table() and pd.crosstab()
- Efficient file I/O – reading large files with chunksize and using parquet for speed
- Pandas options tuning with pd.set_option() for better display and performance
- Suppressing scientific notation using pd.set_option('display.float_format', '{:.2f}'.format)



## 📚 Resources
- NumPy Documentation: https://numpy.org/doc/
- Pandas Documentation: https://pandas.pydata.org/docs/
- Kaggle Datasets: https://www.kaggle.com/datasets

Happy Coding! 🚀