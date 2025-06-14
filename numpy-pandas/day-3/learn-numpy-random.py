# NumPy's random module
# This module is used for generating random numbers, arrays, and performing simulations.

#  Commonly Used Functions
# | Function              | Description                                                             |
# | --------------------- | ----------------------------------------------------------------------- |
# | `np.random.rand()`    | Generate random numbers from a **uniform distribution** between 0 and 1 |
# | `np.random.randn()`   | Generate random numbers from a **normal distribution** (mean=0, std=1)  |
# | `np.random.randint()` | Generate random integers within a specified range                       |
# | `np.random.choice()`  | Randomly pick values from a given array                                 |
# | `np.random.shuffle()` | Shuffle the contents of an array (in-place)                             |
# | `np.random.seed()`    | Set the random seed for reproducibility                                 |

#  Uniform Distribution
import numpy as np

# 1D array with 5 random floats between 0 and 1
a = np.random.rand(5)
print(a)

# Normal Distribution
# 2D array with values from a standard normal distribution
b = np.random.randn(2, 3)
print(b)

#  Random Integers
# 5 random integers between 10 and 50
c = np.random.randint(10, 50, size=5)
print(c)

# Random Choice
arr = [1, 2, 3, 4, 5]
choice = np.random.choice(arr, size=3, replace=False)  # sample 3 unique items
print(choice)

# Shuffle
arr = np.array([10, 20, 30, 40, 50])
np.random.shuffle(arr)
print(arr)

#  Seed

np.random.seed(42)  # Set seed for reproducibility
print(np.random.rand(3))  # Will always give same result

# Tip: Difference Between rand, randn, and random
# | Function   | Distribution      | Range                                                |
# | ---------- | ----------------- | ---------------------------------------------------- |
# | `rand()`   | Uniform           | \[0, 1)                                              |
# | `randn()`  | Normal (Gaussian) | Mean = 0, Std = 1                                    |
# | `random()` | Uniform           | \[0, 1) (similar to `rand`, but different API style) |


# Commonly Used Functions
# | Function        | Description                                  | Example                                           | Use Case                            |
# | --------------- | -------------------------------------------- | ------------------------------------------------- | ----------------------------------- |
# | `rand()`        | Uniform distribution \[0, 1)                 | `np.random.rand(3)`                               | Generate random float array         |
# | `randn()`       | Standard normal distribution (mean=0, std=1) | `np.random.randn(2, 2)`                           | Simulate normal noise               |
# | `random()`      | Uniform \[0, 1)                              | `np.random.random(4)`                             | Generic random sampling             |
# | `randint()`     | Random integers in a given range             | `np.random.randint(1, 10, size=5)`                | Random IDs                          |
# | `choice()`      | Random selection from array                  | `np.random.choice([1, 2, 3], 2)`                  | Random sampling without replacement |
# | `shuffle()`     | Shuffle array in-place                       | `arr = np.array([1,2,3]); np.random.shuffle(arr)` | Randomize order                     |
# | `permutation()` | Randomly permute array                       | `np.random.permutation(5)`                        | Shuffling while returning new array |
# | `seed()`        | Seed the random number generator             | `np.random.seed(42)`                              | Ensure reproducibility              |

# Discrete Distributions
# | Function                               | Description              | Example                                      | Use Case                     |
# | -------------------------------------- | ------------------------ | -------------------------------------------- | ---------------------------- |
# | `binomial(n, p)`                       | Binomial distribution    | `np.random.binomial(10, 0.5, 5)`             | Simulate coin tosses         |
# | `poisson(lam)`                         | Poisson distribution     | `np.random.poisson(5, 10)`                   | Events per interval          |
# | `geometric(p)`                         | Geometric distribution   | `np.random.geometric(0.5, 5)`                | Failures before success      |
# | `hypergeometric(ngood, nbad, nsample)` | Hypergeometric           | `np.random.hypergeometric(5, 2, 3, 5)`       | Sampling without replacement |
# | `multinomial(n, pvals)`                | Multinomial distribution | `np.random.multinomial(10, [0.2, 0.3, 0.5])` | Multi-outcome events         |
# | `negative_binomial(n, p)`              | Negative binomial        | `np.random.negative_binomial(5, 0.5, 5)`     | Failures until r successes   |

# Continuous Distributions
# | Function                        | Description                 | Example                             | Use Case                     |
# | ------------------------------- | --------------------------- | ----------------------------------- | ---------------------------- |
# | `uniform(low, high)`            | Uniform distribution        | `np.random.uniform(1.0, 10.0, 5)`   | Even random values in range  |
# | `normal(loc, scale)`            | Normal distribution         | `np.random.normal(0, 1, 5)`         | Gaussian noise               |
# | `standard_normal()`             | Standard normal             | `np.random.standard_normal(4)`      | Zero-mean normal values      |
# | `beta(a, b)`                    | Beta distribution           | `np.random.beta(0.5, 0.5, 5)`       | Bayesian modeling            |
# | `gamma(shape)`                  | Gamma distribution          | `np.random.gamma(2.0, 2.0, 5)`      | Modeling wait times          |
# | `chi-square(df)`                | Chi-squared distribution    | `np.random.chisquare(2, 5)`         | Hypothesis testing           |
# | `exponential(scale)`            | Exponential distribution    | `np.random.exponential(1.0, 5)`     | Model inter-arrival times    |
# | `laplace(loc, scale)`           | Laplace distribution        | `np.random.laplace(0, 1, 5)`        | Double exponential noise     |
# | `logistic(loc, scale)`          | Logistic distribution       | `np.random.logistic(0, 1, 5)`       | Logistic regression noise    |
# | `lognormal(mean, sigma)`        | Log-normal distribution     | `np.random.lognormal(0.0, 1.0, 5)`  | Model skewed distributions   |
# | `triangular(left, mode, right)` | Triangular distribution     | `np.random.triangular(1, 5, 10, 5)` | Estimate based modeling      |
# | `vonmises(mu, kappa)`           | Von Mises (circular normal) | `np.random.vonmises(0.0, 4.0, 5)`   | Angle-based stats            |
# | `weibull(a)`                    | Weibull distribution        | `np.random.weibull(2.0, 5)`         | Life data modeling           |
# | `pareto(a)`                     | Pareto distribution         | `np.random.pareto(3.0, 5)`          | Wealth distribution modeling |
# | `f(dfnum, dfden)`               | F-distribution              | `np.random.f(5, 2, 5)`              | ANOVA testing                |
