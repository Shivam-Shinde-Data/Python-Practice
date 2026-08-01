import pandas as pd

# ---------------------------------------
# Exercise 1 - Create a DataFrame
# ---------------------------------------

fruits = pd.DataFrame({
    "Apples": [30],
    "Bananas": [21]
})

print(fruits)


# ---------------------------------------
# Exercise 2 - Create a DataFrame with Index
# ---------------------------------------

fruit_sales = pd.DataFrame(
    {
        "Apples": [35, 41],
        "Bananas": [21, 34]
    },
    index=["2017 Sales", "2018 Sales"]
)

print(fruit_sales)


# ---------------------------------------
# Exercise 3 - Create a Series
# ---------------------------------------

ingredients = pd.Series(
    ["4 cups", "1 cup", "2 large", "1 can"],
    index=["Flour", "Milk", "Eggs", "Spam"],
    name="Dinner"
)

print(ingredients)


# ---------------------------------------
# Exercise 4 - Read CSV
# ---------------------------------------

reviews = pd.read_csv(
    "../input/wine-reviews/winemag-data_first150k.csv",
    index_col=0
)

print(reviews.head())


# ---------------------------------------
# Exercise 5 - Save CSV
# ---------------------------------------

animals = pd.DataFrame(
    {
        "Cows": [12, 20],
        "Goats": [22, 19]
    },
    index=["Year 1", "Year 2"]
)

animals.to_csv("cows_and_goats.csv")
