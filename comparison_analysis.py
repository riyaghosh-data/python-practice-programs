import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("product_comparison.csv")

print(df)

# Calculate growth
df["Growth"] = df["Sales_2026"] - df["Sales_2025"]

print("\nGrowth Analysis:")
print(df[["Category", "Growth"]])

# Visualization
x = range(len(df["Category"]))

plt.bar(x, df["Sales_2025"], width=0.4, label="2025")
plt.bar([i + 0.4 for i in x], df["Sales_2026"], width=0.4, label="2026")

plt.xticks([i + 0.2 for i in x], df["Category"])

plt.title("Sales Comparison by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.legend()
plt.show()