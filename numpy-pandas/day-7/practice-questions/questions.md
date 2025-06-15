
# 🐍 NumPy and Pandas in Python Day 7 – Practice Questions

## 🟢 Beginner Level Questions

1. Demonstrate vectorization by replacing a loop that squares numbers with NumPy operations.
2. Show an example where `.copy()` prevents SettingWithCopyWarning.
3. Measure the execution time of a loop vs. vectorized operation using `%timeit`.
4. Create a simple line plot using Matplotlib and Seaborn.
5. Plot a Pandas DataFrame with `.plot()` and compare with Seaborn.
6. Reduce DataFrame memory usage by converting int64 to int8 where applicable.
7. Use `.loc[]` instead of chained indexing to safely modify data.
8. Convert a column to categorical type and inspect memory usage.
9. Parse a string column into datetime and extract year and month.
10. Create a simple MultiIndex DataFrame with two levels and access a sub-part using `.loc[]`.

---

## 🟡 Intermediate Level Questions

1. Create a pivot table summarizing sales by region and product.
2. Use `pd.crosstab()` to analyze gender distribution across departments.
3. Load a large CSV file using `chunksize`, calculate a running average, and aggregate the result.
4. Convert a large CSV to Parquet format and reload it using Pandas.
5. Customize Pandas output to display 2 decimal float values and 100 rows max.
6. Demonstrate suppression of scientific notation in a DataFrame display.
7. Create a MultiIndex DataFrame and perform groupby at one level.
8. Handle missing datetime values and extract week, day from a datetime column.
9. Compare memory usage before and after converting object columns to categorical.
10. Write a utility that configures Pandas display settings for better readability.

---

## 🔴 Advanced Level Questions


1. Benchmark performance of for-loop vs. vectorized operations on a 1M-row DataFrame.
2. Analyze impact of using `.copy()` in chained assignments when working with slices.
3. Use `%timeit` to optimize a function that cleans and standardizes a DataFrame.
4. Create a plot with dual axes using Matplotlib and annotate key points.
5. Build a custom plotting template using Seaborn's FacetGrid.
6. Tune memory usage on a large dataset with mixed datatypes using `astype()`.
7. Demonstrate chained indexing issues by replicating and resolving a real-world warning.
8. Build a MultiIndex DataFrame and reshape it using `stack()` and `unstack()`.
9. Use pivot_table with multiple aggregation functions (mean, count) and custom fill values.
10. Configure Pandas to use `numba` and `bottleneck` backends and measure performance boost.

---
