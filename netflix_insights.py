import pandas as pd

# Load dataset
df = pd.read_csv("netflix_titles.csv")

print("Total Titles:", len(df))

print("\nMovies vs TV Shows:")
print(df["type"].value_counts())

print("\nRatings:")

print("\nMost Common Ratings:")
print(df["rating"].value_counts().head(5))

print(df["rating"].value_counts())
