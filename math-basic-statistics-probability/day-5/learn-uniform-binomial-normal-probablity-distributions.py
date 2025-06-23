# 🔸 Probability Distributions

# ✅ What is a Probability Distribution?
# A probability distribution tells us how likely different outcomes are in a random experiment.
# There are two main types:
# | Type           | Examples                     |
# | -------------- | ---------------------------- |
# | **Discrete**   | Binomial, Bernoulli, Poisson |
# | **Continuous** | Uniform, Normal, Exponential |

# Let’s go over 3 most common distributions for ML:

# ① Uniform Distribution 📏
# Every outcome is equally likely.
# Example: Rolling a fair die: P(1) = P(2) = ... = P(6) = 1/6

import numpy as np
import matplotlib.pyplot as plt

data = np.random.uniform(low=0.0, high=1.0, size=10000)
plt.hist(data, bins=50, density=True)
plt.title("Uniform Distribution")
plt.show()

# ② Binomial Distribution 🎯
# Used when there are 2 outcomes: success/failure
# Think: Coin toss, Yes/No, Win/Lose
# Parameters:
#     n = number of trials
#     p = probability of success

from scipy.stats import binom

n, p = 10, 0.5  # 10 tosses, fair coin
x = np.arange(0, n+1)
pmf = binom.pmf(x, n, p)

plt.bar(x, pmf)
plt.title("Binomial Distribution (n=10, p=0.5)")
plt.xlabel("Number of Successes")
plt.ylabel("Probability")
plt.show()

# ③ Normal Distribution 🛎️ (Bell Curve)
# Most important in ML
# Data is symmetrically distributed around the mean
# Controlled by:
#     μ = mean
#     σ = standard deviation

from scipy.stats import norm

x = np.linspace(-4, 4, 1000)
pdf = norm.pdf(x, 0, 1)

plt.plot(x, pdf)
plt.title("Normal Distribution (mean=0, std=1)")
plt.xlabel("x")
plt.ylabel("Density")
plt.grid()
plt.show()

# | Distribution | Type                | Example Use Case                |
# | ------------ | ------------------- | ------------------------------- |
# | Uniform      | Discrete/Continuous | Random number generators        |
# | Binomial     | Discrete            | Tossing coins, binary outcome   |
# | Normal       | Continuous          | Heights, exam scores, ML models |
