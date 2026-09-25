# **Data Cleaning**

### **1. Definition**

Data cleaning (or data preprocessing) is the process of detecting, correcting, or removing inaccurate, inconsistent, or missing data from a dataset to improve its quality and reliability.

---

### **2. Importance of Data Cleaning**

- Improves accuracy of analysis and ML models
- Handles missing and noisy data
- Ensures consistency and uniformity
- Removes duplicates and irrelevant data
- Prepares data for visualization and modeling

---

### **3. Common Data Issues**

1. Missing values (NaN, None)
2. Duplicate rows
3. Incorrect data types
4. Outliers
5. Inconsistent formatting (e.g., "Male", "male")
6. Invalid data entries

---

### **4. Handling Missing Values**

#### **4.1 Detect Missing Values**

```cpp
df.isnull()
df.isnull().sum()
```

#### **4.2 Drop Missing Values**

```cpp
df.dropna()              // remove rows with null
df.dropna(axis=1)       // remove columns with null
```

#### **4.3 Fill Missing Values**

```cpp
df.fillna(0)
df.fillna(method="ffill")   // forward fill
df.fillna(method="bfill")   // backward fill
```

#### **4.4 Replace with Mean/Median**

```cpp
df["age"].fillna(df["age"].mean())
```

---

### **5. Removing Duplicates**

#### **5.1 Detect Duplicates**

```cpp
df.duplicated()
```

#### **5.2 Remove Duplicates**

```cpp
df.drop_duplicates()
```

---

### **6. Data Type Conversion**

#### **6.1 Check Data Types**

```cpp
df.dtypes
```

#### **6.2 Convert Data Types**

```cpp
df["age"] = df["age"].astype(int)
df["date"] = pd.to_datetime(df["date"])
```

---

### **7. Handling Outliers**

#### **7.1 Detect Outliers (Simple Method)**

```cpp
df.describe()
```

#### **7.2 Remove Outliers (Using Condition)**

```cpp
df = df[df["age"] < 100]
```

#### **7.3 Using IQR Method**

```cpp
Q1 = df["age"].quantile(0.25)
Q3 = df["age"].quantile(0.75)
IQR = Q3 - Q1

df = df[(df["age"] >= Q1 - 1.5*IQR) & (df["age"] <= Q3 + 1.5*IQR)]
```

---

### **8. Handling Inconsistent Data**

#### **8.1 String Cleaning**

```cpp
df["name"] = df["name"].str.lower()
df["name"] = df["name"].str.strip()
```

#### **8.2 Replace Values**

```cpp
df["gender"].replace({"M": "Male", "F": "Female"})
```

---

### **9. Renaming Columns**

```cpp
df.rename(columns={"old_name": "new_name"})
```

---

### **10. Filtering Invalid Data**

```cpp
df = df[df["age"] > 0]
```

---

### **11. Index Cleaning**

```cpp
df.reset_index(drop=True)
```

---

### **12. Handling Special Characters**

```cpp
df["salary"] = df["salary"].replace("[₹,]", "", regex=True).astype(float)
```

---

### **13. Applying Functions (Custom Cleaning)**

```cpp
df["col"] = df["col"].apply(lambda x: x.strip())
```

---

### **14. Example Workflow (Complete Cleaning Pipeline)**

```cpp
#include <iostream>
using namespace std;

// Pseudocode style representation of Pandas cleaning steps

int main() {
    // 1. Load data
    // df = pd.read_csv("data.csv")

    // 2. Remove duplicates
    // df.drop_duplicates()

    // 3. Handle missing values
    // df.fillna(method="ffill")

    // 4. Convert datatypes
    // df["age"] = df["age"].astype(int)

    // 5. Remove outliers
    // df = df[df["age"] < 100]

    // 6. Clean strings
    // df["name"] = df["name"].str.lower().str.strip()

    // 7. Reset index
    // df.reset_index(drop=True)

    return 0;
}
```

---

### **15. Summary**

Data cleaning in Pandas involves:

- Detecting and handling missing values
- Removing duplicates
- Fixing data types
- Cleaning text data
- Handling outliers
- Ensuring consistency

---

# **Handling Missing Data in Pandas**

### **1. Definition**

Missing data refers to the absence of values in a dataset, typically represented as:

- `NaN` (Not a Number)
- `None`

Handling missing data is essential to ensure data integrity and accurate analysis.

---

### **2. Types of Missing Data**

1. **MCAR (Missing Completely at Random)**
   Missing values occur randomly with no pattern.

2. **MAR (Missing at Random)**
   Missingness depends on other columns.

3. **MNAR (Missing Not at Random)**
   Missingness depends on the missing value itself.

---

### **3. Detecting Missing Values**

#### **3.1 Check Entire DataFrame**

```cpp
df.isnull()
df.isna()
```

#### **3.2 Count Missing Values**

```cpp
df.isnull().sum()
```

#### **3.3 Check Non-Missing**

```cpp
df.notnull()
```

---

### **4. Removing Missing Data**

#### **4.1 Drop Rows with Missing Values**

```cpp
df.dropna()
```

#### **4.2 Drop Columns with Missing Values**

```cpp
df.dropna(axis=1)
```

#### **4.3 Conditional Dropping**

```cpp
df.dropna(thresh=2)  // keep rows with at least 2 non-null values
```

#### **4.4 Drop Specific Columns**

```cpp
df.dropna(subset=["age"])
```

---

### **5. Filling Missing Values (Imputation)**

#### **5.1 Fill with Constant Value**

```cpp
df.fillna(0)
df.fillna("Unknown")
```

---

#### **5.2 Forward Fill (Propagation)**

```cpp
df.fillna(method="ffill")
```

- Uses previous row value
- Useful in time-series data

---

#### **5.3 Backward Fill**

```cpp
df.fillna(method="bfill")
```

- Uses next row value

---

### **5.4 Fill with Mean / Median / Mode**

#### Mean (Numerical Data)

```cpp
df["age"].fillna(df["age"].mean())
```

#### Median (Robust to Outliers)

```cpp
df["age"].fillna(df["age"].median())
```

#### Mode (Categorical Data)

```cpp
df["gender"].fillna(df["gender"].mode()[0])
```

---

## **6. Interpolation (Advanced Filling)**

```cpp
df.interpolate()
```

- Estimates missing values based on trends
- Common in time-series or continuous data

---

## **7. Replace Missing Values Conditionally**

```cpp
df["age"] = df["age"].fillna(0)
```

---

## **8. Using Group-Based Filling**

```cpp
df["salary"] = df.groupby("department")["salary"].transform(
    lambda x: x.fillna(x.mean())
)
```

- Fills missing values based on group statistics

---

## **9. Detecting Missing Data Percentage**

```cpp
(df.isnull().sum() / len(df)) * 100
```

---

## **10. Handling Missing Data Strategy (Important for Exams)**

| Situation           | Best Method           |
| ------------------- | --------------------- |
| Few missing values  | Drop rows             |
| Many missing values | Fill (impute)         |
| Time-series data    | Forward/Backward fill |
| Numerical data      | Mean/Median           |
| Categorical data    | Mode                  |
| Pattern-based       | Interpolation         |

---

## **11. Example Workflow**

```cpp
#include <iostream>
using namespace std;

// Pseudocode for missing data handling

int main() {
    // df = pd.read_csv("data.csv")

    // Detect missing
    // df.isnull().sum()

    // Fill numeric
    // df["age"].fillna(df["age"].mean())

    // Fill categorical
    // df["city"].fillna("Unknown")

    // Forward fill (if needed)
    // df.fillna(method="ffill")

    // Drop remaining
    // df.dropna()

    return 0;
}
```

---
