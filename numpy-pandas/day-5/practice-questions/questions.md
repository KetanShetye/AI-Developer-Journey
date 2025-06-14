
# 🐍 NumPy and Pandas in Python Day 5 – Practice Questions

## 🟢 Beginner Level Questions

1. Detect missing values in a DataFrame using `isna()` and count total missing.
2. Fill all missing numeric values with 0 using `fillna()`.
3. Remove all rows with any missing values using `dropna()`.
4. Check for duplicate rows using `duplicated()`.
5. Remove duplicate rows using `drop_duplicates()`.
6. Convert a column from string to float using `astype()`.
7. Convert a date column to datetime format with `pd.to_datetime()`.
8. Use `.str.lower()` to normalize a column of string data.
9. Count the length of each string in a column using `.str.len()`.
10. Add 10% GST to a price column using `.apply()`.

---

## 🟡 Intermediate Level Questions

1. Fill missing values in a specific column using forward-fill (`method='ffill'`).
2. Replace missing values using the mean of a column.
3. Drop rows where specific columns have missing values.
4. Identify and remove duplicate rows based on a subset of columns.
5. Convert multiple columns to appropriate dtypes (e.g., string, int).
6. Extract domain names from an email column using `.str.extract()`.
7. Create a new column from combined values using `.str` operations.
8. Use `.apply()` with a custom function to classify rows.
9. Apply a row-wise function to compute a weighted score.
10. Use `pd.to_numeric()` with error coercion to clean invalid data.

---

## 🔴 Advanced Level Questions

1. Fill missing values conditionally based on group means (e.g., per category).
2. Handle missing values using interpolation.
3. Deduplicate large datasets with performance optimization.
4. Create a custom function to correct common string typos with `.apply()`.
5. Vectorize string cleaning operations instead of using `.apply()`.
6. Apply multiple transformations using `.applymap()` on DataFrame.
7. Parse and normalize a JSON string column using `json.loads` and `.apply()`.
8. Convert complex categorical columns to `category` dtype and analyze memory.
9. Write a reusable function to clean any DataFrame with missing/invalid data.
10. Build a pipeline that combines `fillna`, type conversion, and string cleaning.

---
