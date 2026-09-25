## **1. Definition**

A **DataFrame** in pandas is a **two-dimensional labeled data structure** with rows and columns, capable of storing heterogeneous data types.

- It is analogous to a **table**, **spreadsheet**, or **SQL table**
- Built on top of NumPy

---

## **2. Key Characteristics**

- 2D structure (rows × columns)
- Labeled axes:
  - **Index (rows)**
  - **Columns**

- Can hold **different data types per column**
- Size is mutable (rows/columns can be added or removed)
- Supports vectorized operations

---

## **3. Creation of DataFrame**

### **(a) From Dictionary**

```python
import pandas as pd

data = {
    'Name': ['A', 'B', 'C'],
    'Marks': [85, 90, 78]
}

df = pd.DataFrame(data)
```

---

### **(b) From List of Lists**

```python
data = [
    ['A', 85],
    ['B', 90],
    ['C', 78]
]

df = pd.DataFrame(data, columns=['Name', 'Marks'])
```

---

### **(c) From Series**

```python
s1 = pd.Series([1, 2, 3])
s2 = pd.Series([4, 5, 6])

df = pd.DataFrame({'col1': s1, 'col2': s2})
```

---

## **4. Structure of DataFrame**

Example:

```python
df = pd.DataFrame({
    'Name': ['A', 'B'],
    'Marks': [85, 90]
})
```

Output:

```
   Name  Marks
0    A     85
1    B     90
```

Components:

| Component | Description         |
| --------- | ------------------- |
| Data      | Values inside table |
| Index     | Row labels          |
| Columns   | Column labels       |

---

## **5. Accessing Data**

### **(a) Column Selection**

```python
df['Name']
```

### **(b) Multiple Columns**

```python
df[['Name', 'Marks']]
```

---

### **(c) Row Selection**

#### Using `loc` (label-based)

```python
df.loc[0]
```

#### Using `iloc` (position-based)

```python
df.iloc[0]
```

---

### **(d) Slicing**

```python
df[0:2]
```

---

## **6. Operations on DataFrame**

### **(a) Arithmetic**

```python
df['Marks'] + 5
```

---

### **(b) Conditional Filtering**

```python
df[df['Marks'] > 80]
```

---

### **(c) Adding New Column**

```python
df['Grade'] = ['A', 'A']
```

---

## **7. Important Attributes**

```python
df.shape      # (rows, columns)
df.size       # total elements
df.columns    # column names
df.index      # row labels
df.values     # data
df.dtypes     # data types
```

---

## **8. Handling Missing Data**

```python
import numpy as np

df = pd.DataFrame({
    'A': [1, 2, np.nan],
    'B': [4, np.nan, 6]
})

df.isnull()
df.dropna()
df.fillna(0)
```

---

## **9. Iteration**

```python
for col in df:
    print(col)

for index, row in df.iterrows():
    print(index, row)
```

---

## **10. Advantages of DataFrame**

- Handles large datasets efficiently
- Supports multiple data types
- Easy data cleaning and transformation
- Powerful indexing and filtering
- Integration with file formats (CSV, Excel, SQL)

---

## **11. Real-Life Example**

Student database:

```python
df = pd.DataFrame({
    'Name': ['A', 'B', 'C'],
    'Marks': [85, 90, 78],
    'City': ['Delhi', 'Mumbai', 'Bhopal']
})
```

---

## **12. Difference: Series vs DataFrame**

| Feature   | Series        | DataFrame |
| --------- | ------------- | --------- |
| Dimension | 1D            | 2D        |
| Structure | Single column | Table     |
| Index     | Yes           | Yes       |
| Columns   | No            | Yes       |

---

## **13. Conceptual Diagram**

```
        Name   Marks
Index
0        A      85
1        B      90
2        C      78
```

---

## **14. Key Points for Exams**

- DataFrame = 2D labeled data structure
- Consists of rows (index) and columns
- Built on NumPy arrays
- Supports heterogeneous data
- Core structure in data analysis

---
