# Probability Density Function
# A Probability Density Function is used to describe the likelihood of a continuous random variable taking on a specific range of values.

# Unlike discrete probabilities (like a coin toss), in continuous cases:

# 📌 The probability of any exact value is 0.
# ✅ We calculate the probability over an interval (like between 1.5 and 2.0).

# 🔹 Properties of PDF:
# | Property           | Description                           |
# | ------------------ | ------------------------------------- |
# | Non-negative       | $f(x) \ge 0$ for all x                |
# | Total area = 1     | $\int_{-\infty}^{\infty} f(x) dx = 1$ |
# | Probability = Area | $P(a < X < b) = \int_a^b f(x) dx$     |

# 🔍 Example: Standard Normal Distribution PDF
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

# Generate values
x = np.linspace(-4, 4, 1000)
pdf = norm.pdf(x, loc=0, scale=1)  # mean = 0, std = 1

plt.plot(x, pdf, label='PDF')
plt.title("Normal Distribution PDF")
plt.xlabel("x")
plt.ylabel("Density")
plt.grid()
plt.legend()
plt.show()

# 🔸 Real-world Example:
# A person’s height (say mean = 170 cm, std = 10 cm) follows a normal distribution.
# What is the probability that a random person is between 160 cm and 180 cm?
from scipy.stats import norm

p = norm.cdf(180, loc=170, scale=10) - norm.cdf(160, loc=170, scale=10)
print("P(160cm < Height < 180cm):", round(p, 4))

# P(160cm < Height < 180cm): 0.6826

# 📌 So, PDF gives you the shape of distribution
# and area under the curve gives you actual probabilities.