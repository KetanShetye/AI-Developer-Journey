# ⚙️ Tuning Pandas with pd.set_option()
# Pandas offers a range of configurable options via pd.set_option() to improve data display, readability, and performance during interactive or large-scale work.

# ✅ Syntax:
# pd.set_option('option_name', value)

# 📋 Common Display Options
# | Option                   | Use Case                           | Example                                                  |
# | ------------------------ | ---------------------------------- | -------------------------------------------------------- |
# | `'display.max_rows'`     | Show more/fewer rows in output     | `pd.set_option('display.max_rows', 100)`                 |
# | `'display.max_columns'`  | Show more/fewer columns            | `pd.set_option('display.max_columns', 50)`               |
# | `'display.width'`        | Total output width (in characters) | `pd.set_option('display.width', 1000)`                   |
# | `'display.float_format'` | Format float output                | `pd.set_option('display.float_format', '{:.2f}'.format)` |
# | `'display.max_colwidth'` | Limit string column width          | `pd.set_option('display.max_colwidth', None)`            |

# 🧠 Example: Format Floats & Expand Width
# pd.set_option('display.float_format', '{:.3f}'.format)
# pd.set_option('display.width', 120)

# 🛠 Performance-Related Options
# | Option                      | Purpose                                                                                                      |
# | --------------------------- | ------------------------------------------------------------------------------------------------------------ |
# | `'mode.chained_assignment'` | Warn or raise on chained assignments. Set to `'warn'`, `'raise'`, or `None`. Use `None` to silence warnings. |
# | `'compute.use_bottleneck'`  | Use fast C-backed operations (usually `True`)                                                                |
# | `'compute.use_numba'`       | Use Numba JIT where possible (e.g. rolling/expanding)                                                        |

# pd.set_option('mode.chained_assignment', None)  # silence chained assignment warning
# 🔍 View and Reset Options

# View option value:
# pd.get_option('display.max_rows')

# Reset a specific option:
# pd.reset_option('display.max_rows')

# Reset all:
# pd.reset_option('all')

# 🧠 Best Practices
# | Situation                    | Suggested Setting                             |
# | ---------------------------- | --------------------------------------------- |
# | Viewing wide DataFrames      | `max_columns`, `width`, `colwidth`            |
# | Lots of rows in terminal     | `max_rows = 100` (or `None` for all)          |
# | Cleaner float display        | `float_format = '{:.2f}'.format`              |
# | Avoid SettingWithCopyWarning | `mode.chained_assignment = None` (with care!) |
