# NumPy vs Python Lists — Performance & Features Comparison
# | Feature / Aspect              | NumPy Arrays                                   | Python Lists                         |
# | ----------------------------- | ---------------------------------------------- | ------------------------------------ |
# | **Performance (Speed)**       | 🚀 Much faster (C backend, vectorized)         | 🐢 Slower (loop-based operations)    |
# | **Memory Efficiency**         | Compact and efficient (fixed type)             | More memory overhead (dynamic types) |
# | **Data Type**                 | Homogeneous (all elements same type)           | Heterogeneous (mixed types allowed)  |
# | **Operations**                | Supports vectorized operations (e.g., `a + b`) | Must use loops for element-wise ops  |
# | **Broadcasting**              | ✅ Yes (auto-expands shapes)                    | ❌ No (manual handling needed)        |
# | **Multidimensional Support**  | Native (`ndarray`) with high efficiency        | Manual nesting (e.g., list of lists) |
# | **Functionality**             | Rich API: stats, linear algebra, reshaping     | Limited built-in functionality       |
# | **Indexing & Slicing**        | Advanced (boolean, fancy, slicing)             | Basic slicing only                   |
# | **Speed for Large Datasets**  | Extremely fast                                 | Becomes very slow                    |
# | **Built-in Math Functions**   | Optimized (`np.sum()`, `np.mean()`, etc.)      | Must loop or use `sum()`, etc.       |
# | **Usage in Data Science/ML**  | 📈 Standard (NumPy, Pandas, TensorFlow)        | Rarely used for numerical tasks      |
# | **Interoperability**          | Works with Pandas, SciPy, etc.                 | Needs conversion                     |
# | **Ease of Use (Small tasks)** | Slightly complex                               | Very beginner-friendly               |
# | **Installation**              | Requires `numpy` package                       | Built-in                             |

#  Example: Speed Comparison
import numpy as np
import time

# NumPy
a = np.arange(1_000_000)
start = time.time()
a_sum = np.sum(a)
print("NumPy time:", time.time() - start)

# Python list
b = list(range(1_000_000))
start = time.time()
b_sum = sum(b)
print("List time:", time.time() - start)

# NumPy is usually 5x to 100x faster for large numerical operations.