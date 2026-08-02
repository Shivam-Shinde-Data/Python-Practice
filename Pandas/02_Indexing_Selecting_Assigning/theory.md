# Indexing, Selecting & Assigning

## Introduction

Pandas provides multiple ways to access, filter, and update data. The most commonly used methods are `loc`, `iloc`, and conditional filtering.

---

## Accessing Columns

```python
reviews.country

reviews["country"]
```

Access a single value:

```python
reviews["country"][0]
```

---

## `iloc` (Position-Based)

Select data using row and column positions.

```python
reviews.iloc[0]          # First row
reviews.iloc[:, 0]       # First column
reviews.iloc[:3, 0]      # First 3 rows of first column
reviews.iloc[-5:]        # Last 5 rows
```

---

## `loc` (Label-Based)

Select data using row labels and column names.

```python
reviews.loc[0, "country"]

reviews.loc[:, ["country", "points"]]
```

---

## `loc` vs `iloc`

| `iloc` | `loc` |
|--------|-------|
| Integer positions | Labels |
| End index excluded | End index included |

---

## Filtering Data

Single condition:

```python
reviews.loc[reviews.country == "Italy"]
```

Multiple conditions:

```python
reviews.loc[(reviews.country == "Italy") & (reviews.points >= 90)]

reviews.loc[(reviews.country == "Italy") | (reviews.points >= 90)]
```

Multiple values:

```python
reviews.loc[reviews.country.isin(["Italy", "France"])]
```

Missing values:

```python
reviews.loc[reviews.price.notnull()]

reviews.loc[reviews.price.isnull()]
```

---

## Setting an Index

```python
reviews.set_index("title")
```

---

## Assigning Values

```python
reviews["critic"] = "everyone"

reviews["index_backwards"] = range(len(reviews), 0, -1)
```

---

## Quick Revision

- `reviews["column"]` or `reviews.column` → Select a column
- `iloc` → Position-based indexing
- `loc` → Label-based indexing
- `&` → AND
- `|` → OR
- `isin()` → Multiple values
- `isnull()` / `notnull()` → Missing values
- `set_index()` → Change DataFrame index
- `=` → Create or update a column
