# 🧮 Suppress Scientific Notation in Pandas
# Great! Suppressing scientific notation in Pandas is especially useful when working with large or small float values (e.g., 1.23e+10) that you'd prefer to see as standard decimal numbers.

# ✅ Use pd.set_option() with display.float_format
import pandas as pd
pd.set_option('display.float_format', '{:.2f}'.format)

# 🔍 Example:
df = pd.DataFrame({
    'Amount': [123456789.123456, 0.00000012345]
})
print(df)
# Default Output (Scientific Notation):
#          Amount
# 0  1.234568e+08
# 1  1.234500e-07

# After Setting Float Format:
#        Amount
# 0  123456789.12
# 1          0.00

# 🔧 Custom Format (Optional)
# You can modify the format to suit your precision:
# | Format             | Output Example | Description           |
# | ------------------ | -------------- | --------------------- |
# | `'{:.2f}'.format`  | `1234.57`      | 2 decimal places      |
# | `'{:.6f}'.format`  | `0.000123`     | 6 decimal places      |
# | `'{:,.2f}'.format` | `1,234.57`     | With comma separators |

# 🧠 Note:
# This setting only affects how values are displayed, not the underlying data.
# You can reset using:
# pd.reset_option('display.float_format')
