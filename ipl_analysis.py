import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("ipl_matches.csv")

print(df)

# Count titles
titles = df["Winner"].value_counts()

print("\nIPL Titles:")
print(titles)

# Plot
plt.figure(figsize=(7,5))
plt.bar(titles.index, titles.values)

plt.title("IPL Titles (Sample Dataset)")
plt.xlabel("Team")
plt.ylabel("Titles")

plt.xticks(rotation=20)

plt.tight_layout()
plt.show()