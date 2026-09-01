import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("ecommerce_products.csv")

# Calculate revenue
df["Revenue"] = df["Units_Sold"] * df["Selling_Price"]

# Calculate profit
df["Profit"] = (
    df["Units_Sold"]
    * (df["Selling_Price"] - df["Cost_Price"])
)

# Calculate profit margin
df["Profit_Margin (%)"] = (
    df["Profit"] / df["Revenue"]
) * 100

print(df)

# Category-wise revenue
category_revenue = df.groupby("Category")["Revenue"].sum()

print("\nRevenue by Category:")
print(category_revenue)

# Top product by revenue
top_product = df.loc[df["Revenue"].idxmax()]

print("\nTop Revenue Product:")
print(top_product)

# Top product by profit
top_profit = df.loc[df["Profit"].idxmax()]

print("\nTop Profit Product:")
print(top_profit)

# Visualization
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.bar(df["Product"], df["Revenue"])
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=45)

plt.subplot(1, 2, 2)
plt.bar(df["Product"], df["Profit"])
plt.title("Profit by Product")
plt.xlabel("Product")
plt.ylabel("Profit")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()