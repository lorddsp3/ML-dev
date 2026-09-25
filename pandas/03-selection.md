## Indexing & Selection in Pandas (`loc` vs `iloc`)

This is a **core concept** in pandas for accessing and manipulating data inside a DataFrame. Questions on this typically test precision—label vs position access, slicing behavior, and conditional filtering.

---

# 1. Basic Idea

| Method | Type of Indexing  | Uses                     |
| ------ | ----------------- | ------------------------ |
| `loc`  | **Label-based**   | Uses row/column names    |
| `iloc` | **Integer-based** | Uses numerical positions |

---

# 2. Sample DataFrame

```python
import pandas as pd

data = {
    "name": ["aa", "bb", "cc", "dd"],
    "age": [11, 22, 33, 44],
    "marks": [50, 60, 70, 80]
}

df = pd.DataFrame(data)
print(df)
```

Output:

```
   name  age  marks
0   aa   11     50
1   bb   22     60
2   cc   33     70
3   dd   44     80
```

---

# 3. `loc` → Label-Based Indexing

### Syntax:

```python
df.loc[row_label, column_label]
```

### Key Points:

- Uses **index labels**, not positions
- Both row and column labels must match actual names
- **End index is INCLUDED** in slicing

---

### Examples

#### (1) Get single row

```python
print(df.loc[2])
```

#### (2) Get specific value

```python
print(df.loc[1, "age"])
```

#### (3) Get multiple rows

```python
print(df.loc[1:3])
```

#### (4) Select specific columns

```python
print(df.loc[:, ["name", "marks"]])
```

#### (5) Conditional filtering

```python
print(df.loc[df["age"] > 20])
```

---

# 4. `iloc` → Integer Position-Based Indexing

### Syntax:

```python
df.iloc[row_index, column_index]
```

### Key Points:

- Uses **zero-based integer positions**
- Works like Python lists
- **End index is EXCLUDED** (like slicing)

---

### Examples

#### (1) Get single row

```python
print(df.iloc[2])
```

#### (2) Get specific value

```python
print(df.iloc[1, 1])  # row 1, column 1 → age
```

#### (3) Get multiple rows

```python
print(df.iloc[1:3])
```

#### (4) Select columns

```python
print(df.iloc[:, [0, 2]])
```

---

# 5. Key Differences (Very Important for Exams)

| Feature          | `loc`       | `iloc`     |
| ---------------- | ----------- | ---------- |
| Basis            | Labels      | Positions  |
| Input            | Index names | Integers   |
| Slice End        | Included    | Excluded   |
| Boolean indexing | Yes         | Yes        |
| Error Type       | KeyError    | IndexError |

---

# 6. Example with Custom Index

```python
df.index = ["a", "b", "c", "d"]

print(df.loc["b"])   # works
print(df.iloc[1])    # still works
```

---

# 7. Common Mistakes

### ❌ Mixing labels with `iloc`

```python
df.iloc["a"]   # ERROR
```

### ❌ Using position with `loc`

```python
df.loc[1]  # Works only if index is 0,1,2...
```

---

# 8. Practical Use Cases

### Use `loc` when:

- You know **row/column names**
- You need **conditional filtering**

### Use `iloc` when:

- You want **fast positional access**
- You are doing **numerical slicing**

---

# 9. Combined Example

```python
# Get marks of students with age > 20
print(df.loc[df["age"] > 20, "marks"])

# Get same using iloc (less readable)
print(df.iloc[df["age"].values > 20, 2])
```
