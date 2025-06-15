# ✅ Profiling Performance with %timeit
# incredibly useful when comparing the efficiency of vectorized vs. non-vectorized code (or any two approaches).

# ⏱️ What is %timeit?
# %timeit is a Jupyter/IPython magic command used to measure the execution time of a single line or block of code 
# — it runs the code multiple times and gives you the average execution time, making it more accurate than time.time().

# 🧪 Example 1: Compare loop vs. vectorized NumPy operation
# import numpy as np
# arr = np.arange(1_000_000)

import numpy as np
arr = np.arange(1_000_000)

# ❌ Using Loop (slow):
# %timeit [x * 2 for x in arr]

# ✅ Using Vectorized (fast):
# %timeit arr * 2
# 🔍 You’ll often see that vectorized operations are 10x–100x faster.

# 🧪 Example 2: Pandas .apply() vs Vectorized math
import pandas as pd
df = pd.DataFrame({'a': np.arange(1_000)})

# Using apply
# %timeit df['a'].apply(lambda x: x + 1)

# Using vectorized operation
# %timeit df['a'] + 1

# ✅ The vectorized operation is almost always faster and should be preferred when available.

# 🧪 Block-Level Timing with %%timeit
# For multiple lines, use %%timeit at the top of the code block:
# %%timeit
# result = []
# for i in range(1000):
#     result.append(i ** 2)


# ⚠️ Important Notes
# %timeit only works in IPython/Jupyter environments.
# Avoid testing code with side effects (e.g., file writing) using %timeit.
# It internally runs the code multiple times to give stable and averaged timing.

# 🧠 Tip:
# Use %timeit to:
# Compare performance of NumPy vs native Python
# Evaluate Pandas vectorized vs .apply()
# Optimize data pipelines by identifying slow steps

