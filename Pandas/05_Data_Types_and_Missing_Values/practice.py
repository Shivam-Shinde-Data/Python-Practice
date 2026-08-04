import pandas as pd

reviews = pd.read_csv(
    "../input/wine-reviews/winemag-data-130k-v2.csv",
    index_col=0
)


# 1. Get the data type of the points column.
dtype = reviews.points.dtype


# 2. Convert the points column to strings.
point_strings = reviews.points.astype("str")


# 3. Count reviews with missing prices.
n_missing_prices = reviews.price.isnull().sum()


# 4. Count reviews by region, replacing missing values with "Unknown".
reviews_per_region = reviews.region_1.fillna(
    "Unknown"
).value_counts()
