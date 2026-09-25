## **1. Introduction**

In pandas, input/output operations allow importing and exporting datasets in multiple formats such as **CSV, Excel, and JSON**. These are essential for real-world data handling and preprocessing.

---

## **2. CSV Files**

### **(a) Reading CSV File**

```python
import pandas as pd

df = pd.read_csv("data.csv")
```

#### **Important Parameters**

```python
df = pd.read_csv(
    "data.csv",
    sep=",",          # delimiter
    header=0,         # row as column names
    index_col=0,      # set index column
    usecols=['A','B'],# select columns
    nrows=10          # read limited rows
)
```

---

### **(b) Writing CSV File**

```python
df.to_csv("output.csv", index=False)
```

#### Key Options:

- `index=False` → avoids writing row index
- `columns=[...]` → select specific columns

---

### **(c) Characteristics of CSV**

- Plain text format
- Lightweight and fast
- Widely supported

---

## **3. Excel Files**

### **(a) Reading Excel File**

```python
df = pd.read_excel("data.xlsx")
```

#### With Options:

```python
df = pd.read_excel(
    "data.xlsx",
    sheet_name="Sheet1",
    usecols="A:C",
    skiprows=2
)
```

---

### **(b) Writing Excel File**

```python
df.to_excel("output.xlsx", index=False)
```

#### Multiple Sheets:

```python
with pd.ExcelWriter("output.xlsx") as writer:
    df.to_excel(writer, sheet_name="Sheet1")
```

---

### **(c) Characteristics of Excel**

- Supports multiple sheets
- Rich formatting
- Heavier than CSV

---

## **4. JSON Files**

### **(a) Reading JSON**

```python
df = pd.read_json("data.json")
```

#### With Options:

```python
df = pd.read_json(
    "data.json",
    orient="records"
)
```

---

### **(b) Writing JSON**

```python
df.to_json("output.json", orient="records")
```

---

### **(c) JSON Orient Types**

| Orient  | Description          |
| ------- | -------------------- |
| records | list of dictionaries |
| columns | dict of columns      |
| index   | dict of index        |

---

### **(d) Characteristics of JSON**

- Hierarchical structure
- Used in APIs and web data
- Supports nested data

---

## **5. Comparison Table**

| Feature    | CSV           | Excel                 | JSON         |
| ---------- | ------------- | --------------------- | ------------ |
| Structure  | Flat          | Tabular (multi-sheet) | Hierarchical |
| Size       | Small         | Larger                | Medium       |
| Read Speed | Fast          | Moderate              | Moderate     |
| Use Case   | Data exchange | Reports               | Web/API      |

---

## **6. Practical Example**

```python
# Read CSV
df = pd.read_csv("students.csv")

# Process data
df['Marks'] = df['Marks'] + 5

# Save to Excel
df.to_excel("students_updated.xlsx", index=False)
```

---

## **7. Advantages of Pandas I/O**

- Supports multiple formats
- Fast and efficient
- Easy preprocessing pipeline
- Integrates with databases and APIs

---
