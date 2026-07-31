# Creating, Reading and Writing

## Introduction

Pandas is a Python library used for data analysis and manipulation. It provides powerful data structures like **DataFrame** and **Series** to work with structured data efficiently.

```python
import pandas as pd
```

---

## DataFrame

A **DataFrame** is a two-dimensional table made up of rows and columns, similar to an Excel sheet or SQL table.

### Create a DataFrame

```python
df = pd.DataFrame({
    "Name": ["Shivam", "Rahul"],
    "Age": [22, 23]
})
```

### Custom Index

```python
df = pd.DataFrame(
    {"Name": ["Shivam", "Rahul"]},
    index=["Student1", "Student2"]
)
```

---

## Series

A **Series** is a one-dimensional labeled array. It can be considered a single column of a DataFrame.

```python
marks = pd.Series(
    [80, 90, 85],
    index=["Math", "Science", "English"],
    name="Shivam"
)
```

---

## DataFrame vs Series

| DataFrame | Series |
|------------|--------|
| Two-dimensional | One-dimensional |
| Rows & Columns | Single Column |
| Represents a dataset | Represents one column |

---

## Reading CSV Files

Read a CSV file:

```python
df = pd.read_csv("data.csv")
```

Use the first column as the index:

```python
df = pd.read_csv("data.csv", index_col=0)
```

Useful functions:

```python
df.head()      # First 5 rows
df.tail()      # Last 5 rows
df.shape       # (rows, columns)
```

---

## Common Functions

| Function | Purpose |
|----------|---------|
| `pd.DataFrame()` | Create DataFrame |
| `pd.Series()` | Create Series |
| `pd.read_csv()` | Read CSV file |
| `head()` | View first 5 rows |
| `tail()` | View last 5 rows |
| `shape` | Get dataset size |

---

## Quick Revision

- Import Pandas using `import pandas as pd`
- **DataFrame** → Table (Rows + Columns)
- **Series** → Single Column
- Use `pd.read_csv()` to load CSV files
- Use `index_col=0` to set the first column as the index
- Use `head()`, `tail()`, and `shape` to inspect the dataset
