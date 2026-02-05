# NumPy Basics Study Guide

## Table of Contents

1. [Introduction to NumPy](#introduction-to-numpy)
2. [Array Creation](#array-creation)
3. [Array Attributes](#array-attributes)
4. [Array Indexing and Slicing](#array-indexing-and-slicing)
5. [Array Operations](#array-operations)
6. [Mathematical Operations](#mathematical-operations)
7. [Array Manipulation](#array-manipulation)
8. [Statistical Operations](#statistical-operations)
9. [Linear Algebra](#linear-algebra)
10. [Random Number Generation](#random-number-generation)
11. [Working with Missing Data](#working-with-missing-data)

---

## Introduction to NumPy

NumPy is the fundamental package for scientific computing in Python. It is a Python library that provides a multidimensional array object (`ndarray`), various derived objects (such as masked arrays and matrices), and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more.

```python
import numpy as np
```

---

## Array Creation

### Creating Arrays from Lists

```python
# 1D array
arr1d = np.array([1, 2, 3, 4, 5])

# 2D array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])

# 3D array
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
```

### Special Array Creation Functions

```python
# Arrays of zeros
zeros_1d = np.zeros(5)                    # [0., 0., 0., 0., 0.]
zeros_2d = np.zeros((3, 4))               # 3x4 array of zeros

# Arrays of ones
ones_1d = np.ones(5)                      # [1., 1., 1., 1., 1.]
ones_2d = np.ones((2, 3))                 # 2x3 array of ones

# Identity matrix
identity = np.eye(3)                      # 3x3 identity matrix

# Arrays with a range
range_arr = np.arange(0, 10, 2)           # [0, 2, 4, 6, 8]
linspace_arr = np.linspace(0, 1, 5)       # [0., 0.25, 0.5, 0.75, 1.]

# Empty array (contains garbage values)
empty_arr = np.empty((2, 2))

# Full array with specific value
full_arr = np.full((2, 3), 7)             # [[7, 7, 7], [7, 7, 7]]

# Random arrays
random_arr = np.random.random((3, 3))     # 3x3 array of random values between 0-1
```

### Array from Existing Data

```python
# Copy array
arr_copy = np.array([1, 2, 3])
arr_copy = arr.copy()                     # Creates a deep copy

# From iterable
from_iter = np.fromiter(range(5), dtype=float)  # [0., 1., 2., 3., 4.]
```

---

## Array Attributes

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Basic attributes
print(arr.ndim)        # 2 (number of dimensions)
print(arr.shape)       # (2, 3) (tuple of array dimensions)
print(arr.size)        # 6 (total number of elements)
print(arr.dtype)       # int64 (data type of elements)
print(arr.itemsize)    # 8 (bytes per element)
print(arr.nbytes)      # 48 (total bytes: size * itemsize)

# Memory information
print(arr.flags)       # Memory layout information
print(arr.data)        # Python buffer object pointing to start of data
```

### Data Types

```python
# Specifying data types
int_arr = np.array([1, 2, 3], dtype=np.int32)
float_arr = np.array([1, 2, 3], dtype=np.float64)
complex_arr = np.array([1, 2, 3], dtype=np.complex128)
bool_arr = np.array([1, 0, 1], dtype=bool)

# Type conversion
float_version = int_arr.astype(np.float64)
```

---

## Array Indexing and Slicing

### Basic Indexing

```python
arr = np.array([10, 20, 30, 40, 50])

# Single element
print(arr[0])          # 10
print(arr[-1])         # 50 (last element)

# 2D array indexing
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[0, 1])     # 2 (row 0, column 1)
print(arr2d[1, -1])    # 6 (row 1, last column)
```

### Slicing

```python
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Basic slicing
print(arr[2:7])        # [2, 3, 4, 5, 6]
print(arr[2:7:2])      # [2, 4, 6] (step size 2)
print(arr[:5])         # [0, 1, 2, 3, 4] (start to index 5)
print(arr[5:])         # [5, 6, 7, 8, 9] (index 5 to end)

# 2D slicing
arr2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(arr2d[0:2, 1:3]) # [[2, 3], [6, 7]] (rows 0-1, columns 1-2)
print(arr2d[:, 1])     # [2, 6, 10] (all rows, column 1)
print(arr2d[1, :])     # [5, 6, 7, 8] (row 1, all columns)
```

### Boolean Indexing

```python
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Boolean masking
mask = arr > 5
print(mask)            # [False, False, False, False, False, True, True, True, True, True]
print(arr[mask])       # [6, 7, 8, 9, 10]

# Multiple conditions
print(arr[(arr > 3) & (arr < 8)])  # [4, 5, 6, 7] (AND)
print(arr[(arr < 3) | (arr > 8)])  # [1, 2, 9, 10] (OR)

# Setting values with boolean indexing
arr[arr > 5] = 0
print(arr)             # [1, 2, 3, 4, 5, 0, 0, 0, 0, 0]
```

### Fancy Indexing

```python
arr = np.array([10, 20, 30, 40, 50, 60, 70])

# Integer array indexing
print(arr[[0, 2, 4]])  # [10, 30, 50]

# 2D fancy indexing
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[[0, 2], [0, 1]])  # [1, 8] (elements at (0,0) and (2,1))
```

---

## Array Operations

### Arithmetic Operations

```python
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

# Element-wise operations
print(a + b)           # [6, 8, 10, 12]
print(a - b)           # [-4, -4, -4, -4]
print(a * b)           # [5, 12, 21, 32] (element-wise multiplication)
print(a / b)           # [0.2, 0.333, 0.428, 0.5]
print(a ** 2)          # [1, 4, 9, 16] (squares)
print(np.sqrt(a))      # [1., 1.414, 1.732, 2.] (square roots)

# In-place operations
a += 1                 # a becomes [2, 3, 4, 5]
a *= 2                 # a becomes [4, 6, 8, 10]
```

### Comparison Operations

```python
a = np.array([1, 2, 3, 4])
b = np.array([2, 2, 3, 5])

print(a == b)          # [False, True, True, False]
print(a != b)          # [True, False, False, True]
print(a < b)           # [True, False, False, True]
print(a >= b)          # [False, True, True, False]
```

### Aggregate Operations

```python
arr = np.array([1, 2, 3, 4, 5])

print(np.sum(arr))     # 15
print(np.mean(arr))    # 3.0
print(np.std(arr))     # 1.414 (standard deviation)
print(np.var(arr))     # 2.0 (variance)
print(np.min(arr))     # 1
print(np.max(arr))     # 5
print(np.argmin(arr))  # 0 (index of minimum)
print(np.argmax(arr))  # 4 (index of maximum)
```

---

## Mathematical Operations

### Basic Mathematical Functions

```python
arr = np.array([1, 4, 9, 16, 25])

# Trigonometric functions
angles = np.array([0, np.pi/2, np.pi])
print(np.sin(angles))  # [0., 1., 0.]
print(np.cos(angles))  # [1., 0., -1.]

# Exponential and logarithmic
print(np.exp(arr))     # Exponential
print(np.log(arr))     # Natural log
print(np.log10(arr))   # Base-10 log

# Power functions
print(np.power(arr, 2))  # Square
print(np.sqrt(arr))     # Square root

# Rounding
arr_float = np.array([1.234, 2.567, 3.899])
print(np.round(arr_float))    # [1., 3., 4.]
print(np.floor(arr_float))    # [1., 2., 3.]
print(np.ceil(arr_float))     # [2., 3., 4.]
```

### Matrix Operations

```python
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Matrix multiplication
print(np.dot(a, b))    # [[19, 22], [43, 50]]
print(a @ b)           # Same as np.dot (Python 3.5+)

# Element-wise multiplication
print(a * b)           # [[5, 12], [21, 32]]

# Transpose
print(a.T)             # [[1, 3], [2, 4]]

# Inverse
print(np.linalg.inv(a)) # Inverse of matrix a
```

---

## Array Manipulation

### Reshaping Arrays

```python
arr = np.arange(12)    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# Reshape
arr_2d = arr.reshape(3, 4)    # 3x4 array
arr_3d = arr.reshape(2, 3, 2) # 2x3x2 array

# Flatten
flat_arr = arr_2d.flatten()   # Back to 1D
ravel_arr = arr_2d.ravel()    # Also flattens (creates view if possible)

# Resize
resized = np.resize(arr, (3, 5))  # Can change total size
```

### Adding/Removing Elements

```python
arr = np.array([1, 2, 3])

# Adding elements
new_arr = np.append(arr, [4, 5])        # [1, 2, 3, 4, 5]
new_arr = np.insert(arr, 1, [10, 20])   # [1, 10, 20, 2, 3]

# Removing elements
removed = np.delete(arr, 1)             # [1, 3] (remove element at index 1)

# Concatenation
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
concat = np.concatenate([a, b])         # [1, 2, 3, 4, 5, 6]

# 2D concatenation
a2d = np.array([[1, 2], [3, 4]])
b2d = np.array([[5, 6], [7, 8]])
vstack = np.vstack([a2d, b2d])          # Vertical stack
hstack = np.hstack([a2d, b2d])          # Horizontal stack
```

### Splitting Arrays

```python
arr = np.arange(10)    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Split into equal parts
split_arr = np.split(arr, 2)            # [array([0,1,2,3,4]), array([5,6,7,8,9])]
split_arr = np.split(arr, [3, 7])       # Split at indices 3 and 7

# 2D splitting
arr2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
vsplit = np.vsplit(arr2d, 3)            # Split vertically
hsplit = np.hsplit(arr2d, 2)            # Split horizontally
```

### Sorting and Searching

```python
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])

# Sorting
sorted_arr = np.sort(arr)               # [1, 1, 2, 3, 4, 5, 6, 9]
argsorted = np.argsort(arr)             # [1, 3, 6, 0, 2, 4, 7, 5] (indices)

# Searching
print(np.where(arr > 4))                # (array([4, 5, 7]),) (indices where condition is True)
print(np.searchsorted([1, 2, 3, 4, 5], 3))  # 2 (index where 3 should be inserted)
```

---

## Statistical Operations

### Basic Statistics

```python
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Central tendency
print(np.mean(arr))        # 5.5
print(np.median(arr))      # 5.5

# Dispersion
print(np.std(arr))         # 2.872 (standard deviation)
print(np.var(arr))         # 8.25 (variance)
print(np.ptp(arr))         # 9 (peak to peak: max - min)

# Percentiles and quantiles
print(np.percentile(arr, 25))  # 3.25 (25th percentile)
print(np.percentile(arr, 75))  # 7.75 (75th percentile)
print(np.quantile(arr, 0.5))   # 5.5 (median)

# 2D statistics
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.mean(arr2d, axis=0))  # [4., 5., 6.] (mean of each column)
print(np.mean(arr2d, axis=1))  # [2., 5., 8.] (mean of each row)
```

### Correlation and Covariance

```python
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

# Correlation coefficient
print(np.corrcoef(x, y))   # Correlation matrix

# Covariance
print(np.cov(x, y))        # Covariance matrix
```

---

## Linear Algebra

### Basic Linear Algebra Operations

```python
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Matrix operations
print(np.dot(a, b))        # Matrix multiplication
print(a @ b)               # Alternative syntax
print(np.linalg.det(a))    # Determinant
print(np.linalg.inv(a))    # Inverse matrix
print(np.linalg.pinv(a))   # Pseudo-inverse

# Eigenvalues and eigenvectors
eigenvals, eigenvecs = np.linalg.eig(a)

# Solving linear equations
# Solve: 3x + y = 9, x + 2y = 8
A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])
x = np.linalg.solve(A, b)  # [2., 3.]

# Norms
print(np.linalg.norm(a))   # Matrix/vector norm
```

### Special Matrices

```python
# Identity matrix
identity = np.eye(3)       # 3x3 identity

# Diagonal matrix
diag = np.diag([1, 2, 3])  # [[1, 0, 0], [0, 2, 0], [0, 0, 3]]

# Triangular matrices
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
upper_tri = np.triu(arr)   # Upper triangular
lower_tri = np.tril(arr)   # Lower triangular
```

---

## Random Number Generation

### Basic Random Numbers

```python
# Random floats in [0.0, 1.0)
random_floats = np.random.random(5)          # 5 random floats
random_2d = np.random.random((3, 3))         # 3x3 array of random floats

# Random integers
random_ints = np.random.randint(0, 10, 5)    # 5 random integers from 0-9
random_ints_2d = np.random.randint(0, 100, (2, 3))  # 2x3 array

# Random choice
choices = np.random.choice([1, 2, 3, 4, 5], size=10)  # 10 random choices

# Shuffling
arr = np.arange(10)
np.random.shuffle(arr)     # Shuffle in-place
```

### Distributions

```python
# Normal distribution
normal = np.random.normal(0, 1, 1000)        # Mean=0, std=1, 1000 samples

# Uniform distribution
uniform = np.random.uniform(0, 1, 1000)      # Min=0, max=1, 1000 samples

# Other distributions
binomial = np.random.binomial(10, 0.5, 1000) # Binomial: n=10, p=0.5
poisson = np.random.poisson(5, 1000)         # Poisson: lambda=5
exponential = np.random.exponential(1, 1000) # Exponential: scale=1
```

### Seeding for Reproducibility

```python
np.random.seed(42)        # Set random seed for reproducibility
random1 = np.random.random(5)

np.random.seed(42)        # Same seed produces same results
random2 = np.random.random(5)

print(np.array_equal(random1, random2))  # True
```

---

## Working with Missing Data

### NaN (Not a Number) Operations

```python
# Creating arrays with NaN
arr_with_nan = np.array([1, 2, np.nan, 4, 5, np.nan])

# Checking for NaN
print(np.isnan(arr_with_nan))          # [False, False, True, False, False, True]

# Operations with NaN
print(np.nansum(arr_with_nan))         # 12 (sum ignoring NaN)
print(np.nanmean(arr_with_nan))        # 3.0 (mean ignoring NaN)
print(np.nanmax(arr_with_nan))         # 5 (max ignoring NaN)

# Removing NaN
clean_arr = arr_with_nan[~np.isnan(arr_with_nan)]  # [1., 2., 4., 5.]
```

### Infinity Operations

```python
arr_with_inf = np.array([1, 2, np.inf, 4, -np.inf])

print(np.isinf(arr_with_inf))          # [False, False, True, False, True]
print(np.isfinite(arr_with_inf))       # [True, True, False, True, False]
```

---

## Advanced Topics

### Broadcasting

```python
# Array with scalar
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr + 5)             # Adds 5 to each element

# Array with different shapes
a = np.array([[1, 2, 3]])           # Shape: (1, 3)
b = np.array([[1], [2], [3]])       # Shape: (3, 1)
print(a + b)               # Result shape: (3, 3)
```

### Vectorization

```python
# Non-vectorized (slow)
def slow_square(arr):
    result = []
    for x in arr:
        result.append(x ** 2)
    return np.array(result)

# Vectorized (fast)
def fast_square(arr):
    return arr ** 2

large_arr = np.random.random(1000000)

# Vectorized operations are much faster
%timeit slow_square(large_arr)  # Slower
%timeit fast_square(large_arr)  # Faster
```
