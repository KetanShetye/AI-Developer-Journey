# Linear Algebra operations in NumPy
# a powerful set of tools for matrix mathematics, widely used in Machine Learning, Computer Graphics, and Scientific Computing.

# Linear Algebra in NumPy (np.linalg)
# All major linear algebra operations in NumPy are under the module np.linalg.

# Common Linear Algebra Functions
# | Function       | Description                                 |
# | -------------- | ------------------------------------------- |
# | `dot(a, b)`    | Matrix or vector multiplication             |
# | `matmul(a, b)` | General matrix multiplication (recommended) |
# | `inv(a)`       | Inverse of a matrix                         |
# | `det(a)`       | Determinant of a matrix                     |
# | `eig(a)`       | Eigenvalues and eigenvectors                |
# | `solve(a, b)`  | Solve linear equation system: `Ax = b`      |
# | `norm(a)`      | Vector or matrix norm                       |
# | `transpose(a)` | Transpose of matrix (same as `a.T`)         |
# | `trace(a)`     | Sum of diagonal elements                    |

# Matrix Multiplication (Dot Product)
import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Dot product
np.dot(A, B)
# or
np.matmul(A, B)

# [[19 22]
#  [43 50]]


# Matrix Inverse
from numpy.linalg import inv

A = np.array([[1, 2], [3, 4]])
A_inv = inv(A)
# NOTE :- ⚠️ Only works for square, non-singular matrices.

# Determinant
from numpy.linalg import det

det_val = det(A)  # -2.0000000000000004

# If det(A) == 0, the matrix is singular (not invertible).

# Eigenvalues and Eigenvectors
from numpy.linalg import eig

values, vectors = eig(A)

# values → eigenvalues
# vectors → eigenvectors (column-wise)

# Solving Linear Equations
# To solve Ax = b:
from numpy.linalg import solve

A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])

x = solve(A, b)  # [2. 3.]

# Norm of a Vector or Matrix
from numpy.linalg import norm

v = np.array([3, 4])
norm(v)  # 5.0 (Euclidean norm)

#  Transpose and Trace
A.T           # Transpose
np.trace(A)   # Sum of diagonal elements: 1 + 4 = 5

# | Function       | Example        | Use Case                      |
# | -------------- | -------------- | ----------------------------- |
# | `dot(a, b)`    | `np.dot(A, B)` | Matrix multiplication         |
# | `inv(a)`       | `inv(A)`       | Find matrix inverse           |
# | `det(a)`       | `det(A)`       | Check if matrix is invertible |
# | `eig(a)`       | `eig(A)`       | PCA, diagonalization          |
# | `solve(a, b)`  | `solve(A, b)`  | Solve systems like Ax = b     |
# | `norm(a)`      | `norm(v)`      | Vector magnitude              |
# | `trace(a)`     | `trace(A)`     | Used in optimization          |
# | `transpose(a)` | `A.T`          | Matrix transformations        |
