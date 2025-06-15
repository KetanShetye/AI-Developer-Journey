# ⚠️ Chained Indexing vs. .loc[] / .iloc[] — Why to Avoid Chained Indexing

# 🧩 What is Chained Indexing?
# Chained indexing is when you use two sets of brackets to access and modify data:
# df[df['col'] > 10]['other_col'] = value  # ❌ Bad practice
# This may seem to work, but Pandas gives a warning:
# SettingWithCopyWarning: 
# A value is trying to be set on a copy of a slice from a DataFrame

# 🚫 Why Chained Indexing is Problematic?
# It's ambiguous: Pandas doesn't know if you're working on a view or a copy
# Modifications might silently fail
# Leads to unpredictable bugs

# ✅ Correct Way: Use .loc[] or .iloc[] for clarity and safety
# 🔹 Example using .loc[]
# ✅ Correct
# df.loc[df['col'] > 10, 'other_col'] = value
# .loc[] ensures you're modifying the original DataFrame, not a temporary view.

# 🔹 .loc[] vs .iloc[]
# | Use case  | Syntax                            | Example            |
# | --------- | --------------------------------- | ------------------ |
# | By labels | `df.loc[row_label, column_label]` | `df.loc[5, 'age']` |
# | By index  | `df.iloc[row_idx, column_idx]`    | `df.iloc[2, 1]`    |

# 🧪 Quick Comparison
# ❌ Chained indexing (unsafe)
# df[df['score'] > 90]['passed'] = True

# ✅ Safe and clear
# df.loc[df['score'] > 90, 'passed'] = True

# 🧠 Best Practice
# ✅ Always use .loc[] or .iloc[] for filtering and assignment.
# ❌ Never assign values using chained indexing like df[cond]['col'] = ....