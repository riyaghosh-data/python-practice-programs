import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("netflix_titles.csv")

print(df.head())

# Count Movies vs TV Shows
content_count = df["type"].value_counts()

print(content_count)

# Visualization
plt.figure(figsize=(6,4))
plt.bar(content_count.index, content_count.values)

plt.title("Netflix Content Distribution")
plt.xlabel("Content Type")
plt.ylabel("Count")

plt.show()