import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("netflix_titles.csv")

# Movies vs TV Shows
content_type = df["type"].value_counts()

# Top 5 ratings
ratings = df["rating"].value_counts().head(5)

# Create dashboard
plt.figure(figsize=(10,5))

# Chart 1
plt.subplot(1,2,1)
plt.pie(
    content_type.values,
    labels=content_type.index,
    autopct="%1.1f%%"
)
plt.title("Movies vs TV Shows")

# Chart 2
plt.subplot(1,2,2)
plt.bar(ratings.index, ratings.values)
plt.title("Top 5 Content Ratings")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()