### **1. Definition**

A **Series** in pandas is a **one-dimensional labeled array** capable of holding homogeneous or heterogeneous data such as integers, floats, strings, or objects.

- It is similar to a **column in a table** or a **1D array with labels (index)**.
- Internally built on top of NumPy arrays.

---

### **2. Key Characteristics**

- 1-dimensional structure
- Contains:
  - **Data values**
  - **Index (labels)**

- Mutable (values can be changed)
- Supports vectorized operations

---

### **3. Syntax / Creation**

```python
import pandas as pd

# From list
s = pd.Series([10, 20, 30, 40])

# With custom index
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])

# From dictionary
s = pd.Series({'a': 10, 'b': 20, 'c': 30})
```

---

### **4. Structure of Series**

A Series consists of two main components:

| Component | Description     |
| --------- | --------------- |
| Values    | Actual data     |
| Index     | Labels for data |

Example:

```python
s = pd.Series([100, 200, 300], index=['x', 'y', 'z'])
```

Output:

```
x    100
y    200
z    300
dtype: int64
```

---

### **5. Accessing Elements**

#### **(a) By Index Label**

```python
print(s['x'])
```

#### **(b) By Position**

```python
print(s[0])
```

#### **(c) Slicing**

```python
print(s[0:2])
```

---

### **6. Operations on Series**

#### **(a) Arithmetic Operations**

```python
s1 = pd.Series([1, 2, 3])
s2 = pd.Series([4, 5, 6])

print(s1 + s2)
```

#### **(b) Scalar Operations**

```python
print(s1 * 2)
```

#### **(c) Conditional Operations**

```python
print(s1[s1 > 1])
```

---

### **7. Important Attributes**

```python
s.index     # returns index
s.values    # returns data
s.dtype     # data type
s.shape     # size of series
s.size      # number of elements
```

---

### **8. Handling Missing Data**

```python
import numpy as np

s = pd.Series([1, 2, np.nan, 4])

print(s.isnull())
print(s.dropna())
```

---

### **9. Advantages of Series**

- Easy data manipulation
- Automatic data alignment
- Efficient handling of missing values
- Supports vectorized operations

---

### **10. Real-Life Example**

Marks of students:

```python
marks = pd.Series([85, 90, 78], index=['A', 'B', 'C'])
```

- A → 85
- B → 90
- C → 78

---

### **11. Difference: Series vs Array**

| Feature     | Series  | Array       |
| ----------- | ------- | ----------- |
| Index       | Present | Not present |
| Labels      | Yes     | No          |
| Flexibility | High    | Lower       |
| Library     | Pandas  | NumPy       |

---

### **12. Diagram (Conceptual)**

```
Index →   a     b     c
        -----------------
Data  →  10    20    30
```

---
