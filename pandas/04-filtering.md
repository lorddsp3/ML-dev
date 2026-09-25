## Filtering & Boolean Masking in pandas

This is a **high-weight concept**: it enables conditional selection of rows based on logical expressions. In exams, focus on syntax, operator rules, and combining conditions.

---

# 1. Definition

**Boolean Masking**:
A technique where a condition is applied to a DataFrame/Series, producing a **True/False array**, which is then used to filter data.

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
```

---

# 3. Basic Filtering

### Condition → returns boolean mask

```python
print(df["age"] > 20)
```

Output:

```
0    False
1    True
2    True
3    True
```

### Apply mask

```python
print(df[df["age"] > 20])
```

---

# 4. Using `loc` with Conditions

```python
print(df.loc[df["marks"] >= 60])
```

✔ Preferred method (clear and readable)

---

# 5. Multiple Conditions (Very Important)

### Syntax rules:

- Use `&` → AND
- Use `|` → OR
- Use `~` → NOT
- Wrap each condition in **parentheses**

---

### Example: AND condition

```python
print(df[(df["age"] > 20) & (df["marks"] > 65)])
```

---

### Example: OR condition

```python
print(df[(df["age"] < 20) | (df["marks"] > 75)])
```

---

### Example: NOT condition

```python
print(df[~(df["age"] > 20)])
```

---

# 6. Selecting Specific Columns After Filtering

```python
print(df.loc[df["age"] > 20, ["name", "marks"]])
```

---

# 7. Filtering with `isin()`

Used when checking multiple values.

```python
print(df[df["name"].isin(["aa", "cc"])])
```

---

# 8. Filtering with `between()`

```python
print(df[df["age"].between(20, 40)])
```

✔ Includes both limits

---

# 9. Filtering with `str` methods (for strings)

```python
print(df[df["name"].str.contains("a")])
```

---

# 10. Query Method (Alternative)

```python
print(df.query("age > 20 and marks > 60"))
```

✔ Cleaner syntax for complex conditions

---

# 11. Modifying Data Using Boolean Mask

```python
df.loc[df["marks"] < 60, "marks"] = 0
print(df)
```

✔ Used for **conditional updates**

---

# 12. Key Rules / Common Mistakes

### ❌ Using `and`, `or` instead of `&`, `|`

```python
df[(df["age"] > 20) and (df["marks"] > 60)]  # ERROR
```

### ❌ Missing parentheses

```python
df[df["age"] > 20 & df["marks"] > 60]  # WRONG
```

### ✔ Correct:

```python
df[(df["age"] > 20) & (df["marks"] > 60)]
```

---

# 13. Internal Working (Conceptual)

- Condition → creates **Boolean Series**
- Pandas aligns this mask with index
- Only rows with `True` are returned
