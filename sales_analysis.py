import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("sales_data.csv")

# Show data
print(df)

# Total sales
total = df["Sales"].sum()
print("Total Sales:", total)

# Highest selling product
top_product = df.loc[df["Sales"].idxmax()]
print("Top Product:", top_product["Product"])

# Visualization
plt.bar(df["Product"], df["Sales"])
plt.title("Sales Analysis")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.show()