import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("website_traffic.csv")

# Basic insights
print("Total Visitors:", df["Visitors"].sum())
print("Average Visitors:", df["Visitors"].mean())

# Highest traffic month
top_month = df.loc[df["Visitors"].idxmax()]
print("\nHighest Traffic Month:", top_month["Month"])

# Trend visualization
plt.plot(df["Month"], df["Visitors"], marker="o")

plt.title("Website Traffic Trend")
plt.xlabel("Month")
plt.ylabel("Visitors")

plt.grid(True)
plt.show()