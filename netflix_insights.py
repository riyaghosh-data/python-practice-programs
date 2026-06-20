import pandas as pd

# Load dataset
df = pd.read_csv("netflix_titles.csv")

print("Total Titles:", len(df))

print("\nMovies vs TV Shows:")
print(df["type"].value_counts())

print("\nTop 10 Countries:")
print(df["country"].value_counts().head(10))

print("\nMost Common Ratings:")
print(df["rating"].value_counts().head(5))

print("\nRecent Releases:")
print(df["release_year"].value_counts().head(10))