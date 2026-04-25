import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("monthly_sales.csv")

# Basic insights
print("Total Sales:", df["Sales"].sum())
print("Average Monthly Sales:", df["Sales"].mean())
print("Best Month:", df.loc[df["Sales"].idxmax(), "Month"])

# Line chart
plt.figure(figsize=(10, 5))
plt.plot(df["Month"], df["Sales"], marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()