import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)


# 1. Select the description column from reviews.
desc = reviews.description


# 2. Select the first value from the description column.
first_description = reviews.description.iloc[0]


# 3. Select the first row of data.
first_row = reviews.iloc[0]


# 4. Select the first 10 values from the description column.
first_descriptions = reviews.description.iloc[:10]


# 5. Select the records with index labels 1, 2, 3, 5, and 8.
sample_reviews = reviews.loc[[1, 2, 3, 5, 8]]


# 6. Select the country, province, region_1, and region_2 columns
#    for records with index labels 0, 1, 10, and 100.
df = reviews.loc[
    [0, 1, 10, 100],
    ["country", "province", "region_1", "region_2"]
]


# 7. Select the country and variety columns of the first 100 records.
df = reviews.loc[:99, ["country", "variety"]]


# 8. Select all wines made in Italy.
italian_wines = reviews.loc[reviews.country == "Italy"]


# 9. Select wines from Australia or New Zealand with at least 95 points.
top_oceania_wines = reviews.loc[
    (reviews.points >= 95) &
    (reviews.country.isin(["Australia", "New Zealand"]))
]
