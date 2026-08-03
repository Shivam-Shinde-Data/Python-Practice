import pandas as pd

pd.set_option("display.max_rows", 5)

reviews = pd.read_csv(
    "../input/wine-reviews/winemag-data-130k-v2.csv",
    index_col=0
)

# 1. Find the median of the points column.
median_points = reviews.points.median()


# 2. Get all unique countries.
countries = reviews.country.unique()


# 3. Count the number of reviews for each country.
reviews_per_country = reviews.country.value_counts()


# 4. Center the price column by subtracting the mean price.
centered_price = reviews.price - reviews.price.mean()


# 5. Find the wine with the highest points-to-price ratio.
bargain_wine = reviews.loc[
    (reviews.points / reviews.price).idxmax(),
    "title"
]


# 6. Count occurrences of "tropical" and "fruity" in descriptions.
descriptor_counts = pd.Series({
    "tropical": reviews.description.str.contains(
        "tropical",
        na=False
    ).sum(),
    "fruity": reviews.description.str.contains(
        "fruity",
        na=False
    ).sum()
})


# 7. Convert wine scores into star ratings.
def stars(row):
    if row.country == "Canada":
        return 3
    elif row.points >= 95:
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1

star_ratings = reviews.apply(stars, axis="columns")
