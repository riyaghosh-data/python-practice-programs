import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("supermarket_sales.csv")

# Calculate revenue
df["Revenue"] = df["Quantity"] * df["Price"]

print(df)

# Category-wise revenue
category_revenue = df.groupby("Category")["Revenue"].sum()

print("\nRevenue by Category:")
print(category_revenue)

# Find best-selling product by quantity
product_quantity = df.groupby("Product")["Quantity"].sum()
best_product = product_quantity.idxmax()

print("\nBest-selling Product:", best_product)

# Dashboard
plt.figure(figsize=(10, 4))

# Revenue chart
plt.subplot(1, 2, 1)
plt.bar(category_revenue.index, category_revenue.values)
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")

# Quantity chart
plt.subplot(1, 2, 2)
plt.bar(product_quantity.index, product_quantity.values)
plt.title("Product Quantity")
plt.xlabel("Product")
plt.ylabel("Quantity")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()