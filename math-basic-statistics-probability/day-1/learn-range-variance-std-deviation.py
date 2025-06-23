# 🔹 1. Range
# The range is the difference between the maximum and minimum values in a dataset.
# range = max-min

# eg:-
# Data: 10, 15, 20, 30, 45
# Max = 45
# Min = 10
# 👉 Range = 45 - 10 = 35

data = [10, 15, 20, 30, 45]

range_value = max(data) - min(data)
print("Range:", range_value)
# ✅ Output: Range: 35

# 🔹 2. Variance
# Variance measures how spread out the data is from the mean.
# For a dataset with values x1,x2,x3,...,xn and mean u, formula is 

# find formula in form of .png file - `variance-formula.png`
# use case :- 
# population :- When you have data for the entire group (e.g., all students in a school)
# sample :- When you have a subset of the population (e.g., 100 students from a city)
# 🔍 Sample uses n - 1 to correct for bias (called Bessel’s correction)
# 🧠 Intuition:
# Variance gives a squared unit (e.g., ₹², cm²), harder to interpret.
# Standard deviation is the square root of variance and in the same unit as data, so easier to understand.

# eg:-
# Data: 4, 8, 6, 5, 3
# calculate mean --> (4+8+6+5+3)/5 = 5.2
# square differnces from mean :- 
    # (4-5.2)^2 =1.44
    # (8-5.2)^2 =7.84   
    # (6-5.2)^2 =0.64
    # (5-5.2)^2 =0.04
    # (3-5.2)^2 =4.84
# total :- 1.44 + 7.84 + 0.64 + 0.04 + 4.84

# population variance = 14.8/5 = 2.96
# sample variance = 14.8/4 = 3.7

import statistics

data = [4, 8, 6, 5, 3]

# Sample variance (default)
sample_var = statistics.variance(data)

# Population variance
population_var = statistics.pvariance(data)

print("Sample Variance:", sample_var)
print("Population Variance:", population_var)


# 🔹 3. Standard Deviation

# The Standard Deviation is the square root of the variance. 
# It tells you how much the data typically deviates from the mean.

# find formula in form of .png file - `standard-deviation-fomula.png`

# A low standard deviation means the data is closely clustered around the mean.
# A high standard deviation means the data is more spread out.

# eg:
# variance = 3.7
# std deviation = ≈1.92 (≈ -> approximately equal to)

import statistics
import math

data = [4, 8, 6, 5, 3]

# Sample standard deviation
sample_std = statistics.stdev(data)

# Population standard deviation
population_std = statistics.pstdev(data)

# Manual using math.sqrt
variance = statistics.variance(data)
manual_std = math.sqrt(variance)

print("Sample Standard Deviation:", sample_std)
print("Population Standard Deviation:", population_std)
print("Manual (sqrt of variance):", manual_std)


# Sample Standard Deviation: 1.9235...
# Population Standard Deviation: 1.7204...
# Manual (sqrt of variance): 1.9235...