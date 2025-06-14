# Reading Data in Pandas
# one of the most common tasks in data analysis.

# Reading Data in Pandas (CSV, Excel, JSON)
# Pandas provides built-in methods to read data from various formats into a DataFrame.

# Reading CSV Files

import pandas as pd

# Read a CSV file
df_csv = pd.read_csv('data.csv')

# Common optional parameters
df_csv = pd.read_csv('data.csv', delimiter=',', header=0, index_col=0)
# Use Case: Loading datasets from Kaggle, exported Excel sheets, databases, etc.

#  Reading Excel Files
# Read an Excel file
df_excel = pd.read_excel('data.xlsx')

# Reading specific sheet
df_sheet = pd.read_excel('data.xlsx', sheet_name='Sheet1')

# 💡 Requires openpyxl or xlrd depending on Excel file version.
# ✅ Use Case: Reading structured reports, business sheets, MIS data, etc.

# Reading JSON Files
# Read a JSON file
df_json = pd.read_json('data.json')

# If JSON is nested or in lines format
df_json_lines = pd.read_json('data.json', lines=True)
# ✅ Use Case: API responses, MongoDB exports, or logs often come in JSON.

# | Format | Function          | Notes                                         |
# | ------ | ----------------- | --------------------------------------------- |
# | CSV    | `pd.read_csv()`   | Most commonly used, supports URL or file      |
# | Excel  | `pd.read_excel()` | Needs additional dependencies like `openpyxl` |
# | JSON   | `pd.read_json()`  | Great for structured/nested data              |

# 🔎 Tip: Reading from URLs
# df_url = pd.read_csv('https://raw.githubusercontent.com/.../file.csv')


# Full List of File Types Supported by Pandas
# | Format                    | Method                | Notes                                                  |
# | ------------------------- | --------------------- | ------------------------------------------------------ |
# | **CSV**                   | `pd.read_csv()`       | Most commonly used                                     |
# | **Excel**                 | `pd.read_excel()`     | `.xls`, `.xlsx` formats                                |
# | **JSON**                  | `pd.read_json()`      | Supports nested/line-separated JSON                    |
# | **SQL**                   | `pd.read_sql()`       | Read from SQL database (via `SQLAlchemy` or `sqlite3`) |
# | **Parquet**               | `pd.read_parquet()`   | Fast, binary format, great for big data                |
# | **Feather**               | `pd.read_feather()`   | Very fast, columnar storage                            |
# | **ORC**                   | `pd.read_orc()`       | Common in Hadoop/Spark (less used)                     |
# | **HTML**                  | `pd.read_html()`      | Extracts tables from HTML pages                        |
# | **Clipboards**            | `pd.read_clipboard()` | Read data copied to your system clipboard              |
# | **Pickle**                | `pd.read_pickle()`    | Load Python objects serialized with `pickle`           |
# | **Stata**                 | `pd.read_stata()`     | Used in econometrics (.dta files)                      |
# | **SAS**                   | `pd.read_sas()`       | For `.sas7bdat` and `.xpt` files                       |
# | **SPSS (via pyreadstat)** | `pd.read_spss()`      | Statistical software format                            |
# | **LaTeX**                 | `pd.read_latex()`     | Read tabular data from LaTeX documents                 |
# | **HDF5**                  | `pd.read_hdf()`       | Hierarchical format for large datasets                 |


# Example: Reading SQL
import sqlite3
conn = sqlite3.connect('example.db')

df_sql = pd.read_sql('SELECT * FROM table_name', conn)

#  Example: Reading from HTML
tables = pd.read_html('https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)')
print(tables[0])  # First table on the page


# | Text-based             | Binary                         | Web/Other                        |
# | ---------------------- | ------------------------------ | -------------------------------- |
# | CSV, JSON, HTML, LaTeX | Parquet, Feather, HDF5, Pickle | Clipboard, SQL, SPSS, Stata, SAS |
