# Grouping and Sorting

## Introduction

Grouping helps us analyze data category-wise. Instead of working with the entire dataset, we can split it into groups and calculate statistics for each group. Pandas also provides sorting methods to organize the results.

---

## groupby()

`groupby()` splits the data into groups based on one or more columns.

Count wines for each point value:

```python
reviews.groupby("points").points.count()
```

Find the minimum price for each point value:

```python
reviews.groupby("points").price.min()
```

Group by multiple columns:

```python
reviews.groupby(["country", "province"])
```

---

## apply()

Apply a custom function to each group.

Example: Get the first reviewed wine from every winery.

```python
reviews.groupby("winery").apply(
    lambda df: df.title.iloc[0]
)
```

---

## agg()

Perform multiple summary functions at once.

```python
reviews.groupby("country").price.agg([len, min, max])
```

Common aggregation functions:
- `len`
- `count`
- `min`
- `max`
- `mean`
- `sum`

---

## Multi-Index

Grouping by multiple columns creates a **MultiIndex**.

```python
reviews.groupby(
    ["country", "province"]
).description.agg([len])
```

Convert it back to a normal DataFrame:

```python
countries_reviewed.reset_index()
```

---

## Sorting Data

Sort rows by column values.

Ascending order:

```python
countries_reviewed.sort_values(by="len")
```

Descending order:

```python
countries_reviewed.sort_values(
    by="len",
    ascending=False
)
```

Sort by multiple columns:

```python
countries_reviewed.sort_values(
    by=["country", "len"]
)
```

Sort by index:

```python
countries_reviewed.sort_index()
```

---

## Common Methods

| Method | Purpose |
|---------|---------|
| `groupby()` | Group data |
| `apply()` | Apply custom function |
| `agg()` | Multiple aggregations |
| `reset_index()` | Convert MultiIndex to normal index |
| `sort_values()` | Sort by column values |
| `sort_index()` | Sort by index |

---

## Quick Revision

- `groupby()` splits data into groups.
- Use summary functions (`count`, `min`, `max`, `mean`) after grouping.
- `apply()` is used for custom operations on each group.
- `agg()` performs multiple calculations together.
- Grouping by multiple columns creates a **MultiIndex**.
- `reset_index()` converts a MultiIndex back to a normal DataFrame.
- `sort_values()` sorts by column values.
- `sort_index()` sorts by index.
