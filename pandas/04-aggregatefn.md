## Aggregate Functions

Aggregate functions are used to **summarize data** by computing a single value from a Series or DataFrame column. They are fundamental in data analysis, reporting, and statistical computation.

---

# 1. Definition

An **aggregate function** takes multiple values and returns a **single summarized result**.

Examples:

- Sum of values
- Average (mean)
- Minimum / Maximum

---

# 2. Sample DataFrame

```cpp
import pandas as pd

data = {
    "name": ["aa", "bb", "cc", "dd"],
    "age": [11, 22, 33, 44],
    "marks": [50, 60, 70, 80]
}

df = pd.DataFrame(data)
```

---

# 3. Common Aggregate Functions

| Function   | Description               |
| ---------- | ------------------------- |
| `sum()`    | Total of values           |
| `mean()`   | Average                   |
| `min()`    | Smallest value            |
| `max()`    | Largest value             |
| `count()`  | Number of non-null values |
| `std()`    | Standard deviation        |
| `var()`    | Variance                  |
| `median()` | Middle value              |

---

# 4. Applying on Single Column

```cpp
print(df["marks"].sum())
print(df["marks"].mean())
print(df["marks"].max())
```

---

# 5. Applying on Entire DataFrame

```cpp
print(df.sum())
print(df.mean())
```

✔ Automatically applied to **numeric columns only**

---

# 6. Multiple Aggregations using `agg()`

```cpp
print(df["marks"].agg(["sum", "mean", "min", "max"]))
```

---

### On multiple columns:

```cpp
print(df.agg({
    "age": ["min", "max"],
    "marks": ["mean", "sum"]
}))
```

---

# 7. Group-wise Aggregation (`groupby`)

Very important for exams.

### Example:

```cpp
data = {
    "dept": ["A", "A", "B", "B"],
    "marks": [50, 60, 70, 80]
}

df = pd.DataFrame(data)

print(df.groupby("dept")["marks"].mean())
```

---

### Multiple aggregations:

```cpp
print(df.groupby("dept")["marks"].agg(["sum", "mean", "max"]))
```

---

# 8. Custom Aggregate Function

```cpp
def range_val(x):
    return x.max() - x.min()

print(df["marks"].agg(range_val))
```

---

# 9. Axis Concept

- `axis = 0` → column-wise (default)
- `axis = 1` → row-wise

```cpp
print(df.sum(axis=1))  # sum of each row
```

---

# 10. Handling Missing Values

By default, aggregate functions **ignore NaN values**

```cpp
df["marks"].mean()  # ignores NaN
```

---

# 11. Descriptive Statistics Shortcut

```cpp
print(df.describe())
```

✔ Gives:

- count, mean, std, min, max, quartiles

---

# 12. Key Differences

| Method           | Use                     |
| ---------------- | ----------------------- |
| Direct (`sum()`) | Single operation        |
| `agg()`          | Multiple operations     |
| `groupby()`      | Aggregation by category |

---

# 13. Real-World Use Cases

- Sales totals and averages
- Performance analysis
- Data summarization
- Feature engineering in ML

---

# 14. Common Mistakes

### ❌ Applying on non-numeric data

```cpp
df["name"].mean()  # ERROR
```

### ❌ Confusing `count()` with `size()`

- `count()` → ignores NaN
- `size()` → includes NaN

# **GroupBy Operations in Pandas**

# **3. Basic Syntax**

```cpp
df.groupby("column_name")
```

---

# **4. Grouping Data**

## **4.1 Single Column Grouping**

```cpp
df.groupby("department")
```

## **4.2 Multiple Columns Grouping**

```cpp
df.groupby(["department", "gender"])
```

---

# **5. Aggregation Functions**

## **5.1 Common Aggregations**

```cpp
df.groupby("department")["salary"].sum()
df.groupby("department")["salary"].mean()
df.groupby("department")["salary"].count()
df.groupby("department")["salary"].max()
df.groupby("department")["salary"].min()
```

---

## **5.2 Multiple Aggregations**

```cpp
df.groupby("department")["salary"].agg(["sum", "mean", "max"])
```

---

## **5.3 Different Aggregations per Column**

```cpp
df.groupby("department").agg({
    "salary": "mean",
    "age": "max"
})
```

---

# **6. Iterating Through Groups**

```cpp
for key, group in df.groupby("department"):
    cout << key << endl;
```

---

# **7. Transformation (Same Shape Output)**

```cpp
df["avg_salary"] = df.groupby("department")["salary"].transform("mean")
```

- Keeps original DataFrame shape
- Useful for feature engineering

---

# **8. Filtering Groups**

```cpp
df.groupby("department").filter(lambda x: x["salary"].mean() > 50000)
```

---

# **9. Applying Custom Functions**

```cpp
df.groupby("department")["salary"].apply(lambda x: x.max() - x.min())
```

---

# **10. Resetting Index After GroupBy**

```cpp
df.groupby("department")["salary"].mean().reset_index()
```

---

# **11. Sorting Grouped Data**

```cpp
df.groupby("department")["salary"].mean().sort_values()
```

---

# **12. GroupBy with Multiple Columns Example**

```cpp
df.groupby(["department", "gender"])["salary"].mean()
```

---

# **13. Practical Example**

### Dataset:

| Name | Dept | Salary |
| ---- | ---- | ------ |
| A    | IT   | 50000  |
| B    | IT   | 60000  |
| C    | HR   | 40000  |

### Code:

```cpp
df.groupby("Dept")["Salary"].mean()
```

### Output:

```
HR → 40000
IT → 55000
```

---

# **14. Advanced Concepts**

## **14.1 Named Aggregation**

```cpp
df.groupby("department").agg(
    avg_salary=("salary", "mean"),
    max_age=("age", "max")
)
```

---

## **14.2 Group Size**

```cpp
df.groupby("department").size()
```

---

## **14.3 Count Non-Null Values**

```cpp
df.groupby("department").count()
```
