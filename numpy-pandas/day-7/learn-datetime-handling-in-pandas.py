# Datetime Handling in Pandas
# essential in time series analysis, finance, logs, and reporting.

# 🛠 Convert Strings to Datetime: pd.to_datetime()
import pandas as pd

df = pd.DataFrame({
    'date_str': ['2024-01-01', '2024-01-02', '2024-01-03']
})

df['date'] = pd.to_datetime(df['date_str'])
# ✅ Now df['date'] is a proper datetime64[ns] object.

# 🧰 .dt Accessor – Work With Date Components
# Once a column is datetime, use .dt to extract parts:
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['weekday'] = df['date'].dt.day_name()
df['week'] = df['date'].dt.isocalendar().week
df['quarter'] = df['date'].dt.quarter

# 🕐 Time Extraction
df['hour'] = df['date'].dt.hour
df['minute'] = df['date'].dt.minute
df['second'] = df['date'].dt.second


# 🔁 Date Arithmetic
df['date_plus_7'] = df['date'] + pd.Timedelta(days=7)
df['days_diff'] = (pd.Timestamp.today() - df['date']).dt.days

# 📏 Filter by Date Range
# df[df['date'] >= '2024-01-02']

# 🧪 Common Scenarios
# 📌 Parse non-standard date formats
# pd.to_datetime(df['col'], format='%d-%m-%Y', errors='coerce')

# 📌 Handling invalid or missing dates
# pd.to_datetime(df['col'], errors='coerce')  # turns invalid into NaT

# 🧠 Best Practices
# | Task                  | Best Tool                     |
# | --------------------- | ----------------------------- |
# | Convert to datetime   | `pd.to_datetime()`            |
# | Extract parts of date | `.dt.year`, `.dt.month`, etc. |
# | Date arithmetic       | `pd.Timedelta`, subtraction   |
# | Handle bad values     | `errors='coerce'`             |
