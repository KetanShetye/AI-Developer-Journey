# Axis-wise Operations in NumPy 
# a super useful concept for applying functions across rows or columns of arrays.

# What is an Axis?
# In NumPy:
# axis=0 → operates down the rows (i.e., column-wise)
# axis=1 → operates across the columns (i.e., row-wise)

# Axis Visualized
# For this array:
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# axis=0 = ⬇ column-wise (↓ down)
# Acts on: [1, 4], [2, 5], [3, 6]

# axis=1 = ➡ row-wise (→ across)
# Acts on: [1, 2, 3], [4, 5, 6]