
# NumPy

## Overview

NumPy (Numerical Python) is a package for numerical computing in Python. 
- Fast
- Memory Efficient
It provides fast, memory-efficient arrays and operations.
- Pandas is built on Numpy

```
pip install numpy
```

---

## Creating Arrays
Numpy lets us create arrays for faster math on vectors and matricies.

```python
import numpy as np

# From a list
a = np.array([1, 2, 3])
print(a)  # [1 2 3]

# 2D array
b = np.array([[1, 2], [3, 4]])
print(b)
#[[1 2]
# [3 4]]
```

There's a number of helper methods to allow us to quickly build out arrays and matricies.

```python
# Predefined arrays
np.zeros((2, 3))         # 2x3 matrix of zeros
np.ones((3, 3))          # 3x3 matrix of ones
np.full((2, 2), 7)       # 2x2 matrix filled with 7
np.eye(3)                # Identity matrix
np.random.rand(2, 3)     # Random numbers from uniform [0, 1)
np.arange(0, 10, 2)      # [0 2 4 6 8]
np.linspace(0, 1, 5)     # 5 evenly spaced values from 0 to 1
```


## Array Ops
Some mathematical operators work on numpy arrays.

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)        # [5 7 9]
print(a * b)        # [ 4 10 18]
print(a ** 2)       # [1 4 9]
print(np.dot(a, b)) # Dot product: 32 (sum of ith elements multiplied)
```


## Slices
We can easily get portions of arrays

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
# array([[1, 2, 3],
#        [4, 5, 6]])


print(arr[0, 1])  # 2. ROW 0 COL 1
print(arr[:, 1])  # [2 5]. COL 1
print(arr[1, :])  # [4 5 6]. ROW 1
print(arr[-1])    # last row
```


## Reshape and Flatten
Often we'll need to reshape and flatten arrays.  ML packages especially require arrays in a certain shape

```python
a = np.arange(6)        # [0 1 2 3 4 5] (like range)
# Turn into a 2x3 matrix
b = a.reshape(2, 3)     # [[0 1 2] [3 4 5]]
# Squish into a 1d array
c = b.flatten()         # [0 1 2 3 4 5]
```


## Aggregates
We can also perform aggregate ops on arrays to get sums, means standard deviations, etc.

```python
a = np.array([[1, 2, 3], [4, 5, 6]])

print(np.sum(a))             # 21
print(np.sum(a, axis=0))     # [5 7 9] (column-wise)
print(np.mean(a))            # 3.5
print(np.std(a))             # standard deviation
print(np.max(a), np.min(a))  # 6 1
```


## Boolean Masking
We have masks, like we did in Pandas.

```python
a = np.array([10, 15, 20, 25])
mask = a > 15
print(mask)         # [False False  True  True]
print(a[mask])      # [20 25]
```

## Summary

- `np.array` creates arrays
- Element-wise operations are fast and easy
- Use slicing, masks, and reshaping to manipulate data
- Aggregation functions: `sum`, `mean`, `std`, etc.
- Broadcasting simplifies operations on different-shaped arrays
