# ✅ Use .copy() to Avoid SettingWithCopyWarning

# ⚠️ What is SettingWithCopyWarning?
# In Pandas, this warning is raised when you're modifying a subset of a DataFrame that may be a "view" and not a real copy of the original data.
# If you try to update values in a slice of a DataFrame without .copy(), Pandas can’t guarantee whether you're modifying the original data or just a temporary view.
# This can lead to unexpected bugs.

# 🧪 Example of the Problem:
import pandas as pd

df = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie'],
                   'score': [85, 62, 90]})

# Filter students who scored above 80
high_scorers = df[df['score'] > 80]

# Try updating the 'score'
high_scorers['score'] = high_scorers['score'] + 5

# ⚠️ Output:
# SettingWithCopyWarning: 
# A value is trying to be set on a copy of a slice from a DataFrame.

# ✅ Correct Way Using .copy():
# high_scorers = df[df['score'] > 80].copy()
# high_scorers['score'] = high_scorers['score'] + 5

# Now, you're explicitly creating a copy, and the warning is gone.

# 🔍 Why It Matters?
# | Without `.copy()`        | With `.copy()`           |
# | ------------------------ | ------------------------ |
# | May modify original data | Always modifies the copy |
# | Risk of unexpected bugs  | Predictable behavior     |
# | Warning may be ignored   | No warning raised        |

# 🧠 Rule of Thumb
# Whenever you filter/select a subset of a DataFrame and plan to modify it, use .copy() to avoid ambiguity.
# subset = df[df['column'] > value].copy()
# subset['another_column'] = new_value