# Summary Functions and Maps

## Introduction

Summary functions help analyze data by calculating statistics such as mean, count, unique values, and frequencies. Mapping functions are used to transform existing data into a new format.

---

# Summary Functions

Pandas provides several built-in functions to quickly summarize data.

## describe()

Returns statistical information about a column.

```python
reviews.points.describe()
```

For numeric columns, it returns:
- Count
- Mean
- Standard Deviation
- Minimum
- Quartiles (25%, 50%, 75%)
- Maximum

For object (string) columns, it returns:
- Count
- Unique values
- Most frequent value
- Frequency

```python
reviews.taster_name.describe()
```

---

## mean()

Returns the average value.

```python
reviews.points.mean()
```

---

## unique()

Returns all unique values in a column.

```python
reviews.taster_name.unique()
```

---

## value_counts()

Returns each unique value along with its occurrence count.

```python
reviews.taster_name.value_counts()
```

---

# Mapping Data

Mapping is used to transform existing values into new values.

## map()

Applies a function to every value in a Series.

```python
review_points_mean = reviews.points.mean()

reviews.points.map(lambda p: p - review_points_mean)
```

Use `map()` when working with a **single column (Series)**.

---

## apply()

Applies a function to rows or columns of a DataFrame.

```python
def remean_points(row):
    row.points = row.points - review_points_mean
    return row

reviews.apply(remean_points, axis="columns")
```

Use `axis="columns"` to apply the function to each row.

---

# Vectorized Operations

Instead of using `map()` or `apply()`, Pandas supports vectorized operations, which are faster and more efficient.

```python
reviews.points - reviews.points.mean()
```

You can also combine columns directly.

```python
reviews.country + " - " + reviews.region_1
```

---

# Common Functions

| Function | Purpose |
|----------|---------|
| `describe()` | Summary statistics |
| `mean()` | Average value |
| `unique()` | Unique values |
| `value_counts()` | Frequency of values |
| `map()` | Transform a Series |
| `apply()` | Transform DataFrame rows/columns |

---

# map() vs apply()

| map() | apply() |
|--------|----------|
| Works on Series | Works on DataFrame |
| Single value at a time | Entire row or column |
| Simpler transformations | More complex transformations |

---

# Quick Revision

- `describe()` → Summary statistics
- `mean()` → Average value
- `unique()` → Distinct values
- `value_counts()` → Frequency count
- `map()` → Transform a Series
- `apply()` → Transform rows or columns
- Prefer vectorized operations whenever possible because they are faster than `map()` and `apply()`.
