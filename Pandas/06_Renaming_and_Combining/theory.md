# Renaming and Combining

## 1. Renaming
Used to change **column names**, **index values**, or **axis names**.

### Rename Columns
```python
reviews.rename(columns={"points": "score"})
```

### Rename Index Values
```python
reviews.rename(index={0: "firstEntry", 1: "secondEntry"})
```

### Rename Axis Names
```python
reviews.rename_axis("wines", axis="rows") \
       .rename_axis("fields", axis="columns")
```

### When to Use
- Make column names easier to understand.
- Rename indexes for better readability.
- Change row/column axis labels.

---

## 2. Combining Data

### A. concat()
Combines DataFrames **vertically** (default) or **horizontally**.

```python
pd.concat([df1, df2])
```

**Use when:**
- Both DataFrames have the same columns.
- You want to stack rows together.

Example:
```python
all_reviews = pd.concat([canadian_youtube, british_youtube])
```

---

### B. join()
Combines DataFrames using a **common index**.

```python
left.join(right)
```

If both DataFrames have duplicate column names:

```python
left.join(right, lsuffix="_left", rsuffix="_right")
```

Example:
```python
left = canadian_youtube.set_index(["title", "trending_date"])
right = british_youtube.set_index(["title", "trending_date"])

left.join(right, lsuffix="_CAN", rsuffix="_UK")
```

**Use when:**
- DataFrames share the same index.
- You want to add matching columns from another DataFrame.

---

## Quick Comparison

| Function | Purpose |
|----------|---------|
| `rename()` | Rename columns or indexes |
| `rename_axis()` | Rename row/column axis names |
| `concat()` | Stack DataFrames together |
| `join()` | Combine DataFrames using a common index |

---

## Interview Notes

- `rename(columns={})` → Rename column names.
- `rename(index={})` → Rename index values.
- `rename_axis()` → Rename row/column axis labels.
- `concat()` → Stack DataFrames with similar columns.
- `join()` → Combine DataFrames using matching indexes.
- If both DataFrames have the same column names, use **`lsuffix`** and **`rsuffix`** in `join()`.
