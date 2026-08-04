
# Q1. Rename region_1 and region_2 columns

renamed = reviews.rename(columns={
    "region_1": "region",
    "region_2": "locale"
})


# Q2. Set the index name to "wines"

reindexed = reviews.rename_axis("wines")


# Q3. Combine gaming and movie products

combined_products = pd.concat([
    gaming_products,
    movie_products
])



# Q4. Combine powerlifting meets and competitors using MeetID

powerlifting_combined = powerlifting_meets.set_index("MeetID").join(
    powerlifting_competitors.set_index("MeetID")
)
