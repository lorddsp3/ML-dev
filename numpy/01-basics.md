# 1 Why NumPy is Faster than Python Lists

### (1) Contiguous Memory Layout

- NumPy arrays store elements **in continuous memory blocks**
- Python lists store **references (pointers)** to objects

### (2) Homogeneous Data Type

- NumPy arrays → single datatype (e.g., all `int32`)
- Python lists → mixed types allowed

### (3) Vectorization

- NumPy performs operations on **entire arrays at once**
- Python lists require loops

# 1.1 Creating Arrays

### (1) `array()`

Convert list/tuple → NumPy array

```python
import numpy as np

a = np.array([1, 2, 3])
```

### (2) `zeros()`

Creates array filled with 0

```python
np.zeros((2, 3))
```

Output:

```
[[0. 0. 0.]
 [0. 0. 0.]]
```

### (3) `ones()`

Creates array filled with 1

```python
np.ones((2, 2))
```

### (4) `arange()`

Works like Python `range()`

```python
np.arange(0, 10, 2)
```

Output:

```
[0 2 4 6 8]
```

### (5) `linspace()`

Creates evenly spaced numbers between two values

```python
np.linspace(0, 1, 5)
```

Output:

```
[0.   0.25 0.5  0.75 1.  ]
```

➡ Used heavily in plotting and ML

# 1.2 Array Attributes

### (1) `shape`

Returns dimensions of array

```python
a = np.array([[1, 2], [3, 4]])
print(a.shape)
```

Output:

```
(2, 2)
```

---

### (2) `ndim`

Number of dimensions

```python
print(a.ndim)
```

Output:

```
2
```

---

### (3) `dtype`

Data type of elements

```python
print(a.dtype)
```

Output:

```
int64
```

---

### (4) `size`

Total number of elements

```python
print(a.size)
```

Output:

```
4
```
