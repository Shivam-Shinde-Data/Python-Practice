# Data Types and Missing Values

## Introduction

Understanding data types helps you work with data correctly. Pandas also provides simple methods to detect, replace, and handle missing values.

---

## Data Types (`dtype`)

Check the data type of a column:

```python
reviews.price.dtype
```

Check data types of all columns:

```python
reviews.dtypes
```

Common data types:
- `int64` → Integer
- `float64` → Decimal numbers
- `object` → Strings/Text

Check the index data type:

```python
reviews.index.dtype
```

---

## Convert Data Types

Use `astype()` to convert one data type into another.

```python
reviews.points.astype("float64")
```

---

## Missing Data (`NaN`)

`NaN` represents missing values in a dataset.

Find missing values:

```python
pd.isnull(reviews.country)
```

Select rows with missing values:

```python
reviews[pd.isnull(reviews.country)]
```

Check non-missing values:

```python
pd.notnull(reviews.country)
```

---

## Handling Missing Values

Replace missing values with a custom value:

```python
reviews.region_2.fillna("Unknown")
```

`fillna()` is commonly used for cleaning datasets before analysis.

---

## Replacing Values

Replace an existing value with another:

```python
reviews.taster_twitter_handle.replace(
    "@kerinokeefe",
    "@kerino"
)
```

`replace()` is useful for correcting values or replacing placeholders like `"Unknown"` or `"Invalid"`.

---

## Quick Revision

- `dtype` → Data type of a column
- `dtypes` → Data types of all columns
- `astype()` → Convert data type
- `isnull()` → Find missing values
- `notnull()` → Find non-missing values
- `fillna()` → Replace missing values
- `replace()` → Replace existing values
