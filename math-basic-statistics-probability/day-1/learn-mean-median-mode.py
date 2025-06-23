# 🔹 1. Mean (Arithmetic Average)
# The mean of a set of numbers is the sum of all the values divided by the number of values.
# mean = (x1+x2+x3+....+xn)/n

# eg:- 
# Suppose you have scores:
# 50, 60, 70, 80, 90
# mean = (50+60+70+80+90)/5 = 70

data = [50, 60, 70, 80, 90]
mean_value = sum(data) / len(data)
print("Mean:", mean_value)
# ✅ Output: Mean: 70.0

# 🔸 Using Python Libraries:
import statistics
import numpy as np

data = [50, 60, 70, 80, 90]
# Using statistics module
print("Mean (statistics):", statistics.mean(data))
# Using NumPy
print("Mean (NumPy):", np.mean(data))

# 🔹 2. Median
# The median is the middle value in a list of numbers sorted in order.
# If the list has odd number of values: it's the middle value.
# If the list has even number of values: it's the average of the two middle values.

# eg:-
# 🧮 Example 1 (Odd number of elements):
# Data: 3, 7, 9
# Sorted: 3, 7, 9
# 👉 Median = 7 (middle value)

# 🧮 Example 2 (Even number of elements):
# Data: 3, 5, 7, 9
# Sorted: 3, 5, 7, 9
# 👉 Median = (5 + 7) / 2 = 6.0

data_odd = [3, 7, 9]
data_even = [3, 5, 7, 9]

# Manual median for odd-length list
sorted_odd = sorted(data_odd)
n_odd = len(sorted_odd)
median_odd = sorted_odd[n_odd // 2]  # middle value

# Manual median for even-length list
sorted_even = sorted(data_even)
n_even = len(sorted_even)
median_even = (sorted_even[n_even // 2 - 1] + sorted_even[n_even // 2]) / 2

print("Median (odd):", median_odd)
print("Median (even):", median_even)

# Median (odd): 7
# Median (even): 6.0


import statistics
import numpy as np

data_odd = [3, 7, 9]
data_even = [3, 5, 7, 9]

print("Median (statistics, odd):", statistics.median(data_odd))
print("Median (statistics, even):", statistics.median(data_even))

print("Median (NumPy, odd):", np.median(data_odd))
print("Median (NumPy, even):", np.median(data_even))

# 🔹 3. Mode
# The mode is the number that occurs most frequently in a dataset.
# A dataset can have:
    # One mode (unimodal)
    # Multiple modes (multimodal)
    # No mode (if all values are unique)

# eg:-
# 🧮 Example 1:
# Data: 1, 2, 2, 3, 4
# 👉 Mode = 2 (appears twice)

# 🧮 Example 2:
# Data: 1, 2, 2, 3, 3, 4
# 👉 Modes = 2 and 3 (both appear twice → multimodal)

# 🧮 Example 3:
# Data: 1, 2, 3, 4, 5
# 👉 No mode (all unique)

from collections import Counter

data = [1, 2, 2, 3, 3, 4]
counts = Counter(data)
max_count = max(counts.values())
modes = [k for k, v in counts.items() if v == max_count]

print("Mode(s):", modes)
# ✅ Output: Mode(s): [2, 3]

import statistics

data = [1, 2, 2, 3, 3, 4]

try:
    print("Single Mode (statistics):", statistics.mode(data))
except statistics.StatisticsError as e:
    print("Error:", e)

# 🔥 Note: statistics.mode() only returns one value (the first mode), 
# and will raise an error if there are multiple modes with equal frequency.

# 🧠 Alternative: scipy for multimode
from scipy import stats

data = [1, 2, 2, 3, 3, 4]
modes = stats.mode(data, keepdims=False)
print("Mode:", modes.mode, "| Count:", modes.count)

