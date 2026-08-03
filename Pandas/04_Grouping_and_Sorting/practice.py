import pandas as pd

reviews = pd.read_csv(
    "../input/wine-reviews/winemag-data-130k-v2.csv",
    index_col=0
)


# 1. Count how many reviews each reviewer wrote.
reviews_written = reviews.groupby(
    "taster_twitter_handle"
).size()


# 2. Find the highest-rated wine for each price.
best_rating_per_price = reviews.groupby(
    "price"
).points.max()


# 3. Find the minimum and maximum price for each wine variety.
price_extremes = reviews.groupby(
    "variety"
).price.agg(["min", "max"])


# 4. Sort wine varieties by minimum price, then maximum price.
sorted_varieties = price_extremes.sort_values(
    by=["min", "max"],
    ascending=False
)


# 5. Find the average rating given by each reviewer.
reviewer_mean_ratings = reviews.groupby(
    "taster_name"
).points.mean()


# 6. Count wines by country and variety.
country_variety_counts = reviews.groupby(
    ["country", "variety"]
).size().sort_values(ascending=False)
