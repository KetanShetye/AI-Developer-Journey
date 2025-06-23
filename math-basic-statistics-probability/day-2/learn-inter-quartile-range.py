# 🔹 1. Interquartile Range (IQR)
# The Interquartile Range (IQR) measures the middle 50% spread of a dataset.
# It is the difference between the third quartile (Q3) and the first quartile (Q1):
# IQR = Q3 - Q1

# Q1 (25th percentile): Median of the lower half
# Q3 (75th percentile): Median of the upper half

# eg:-
# Data (sorted): 2, 4, 5, 7, 8, 10, 12, 14, 16
# Q1 (lower half): 2, 4, 5, 7 → Median = 4.5
# Q3 (upper half): 10, 12, 14, 16 → Median = 13
# 👉 IQR = 13 - 4.5 = 8.5

import numpy as np

data = [2, 4, 5, 7, 8, 10, 12, 14, 16]

# Sort the data
sorted_data = sorted(data)

# Calculate Q1 and Q3
q1 = np.percentile(sorted_data, 25)
q3 = np.percentile(sorted_data, 75)

iqr = q3 - q1

print("Q1:", q1)
print("Q3:", q3)
print("IQR:", iqr)

# Q1: 4.5
# Q3: 13.0
# IQR: 8.5