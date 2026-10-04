import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("inventory_data.csv")

print(df)

# Total products
print("\nTotal Products:", len(df))

# Total stock
print("Total Stock:", df["Stock"].sum())

# Low stock products
low_stock = df[df["Stock"] < df["Reorder_Level"]]

print("\nLow Stock Products:")
print(low_stock[["Product", "Stock", "Reorder_Level"]])

# Inventory value
df["Inventory_Value"] = df["Stock"] * df["Price"]

print("\nTotal Inventory Value:")
print(df["Inventory_Value"].sum())

# Stock by category
category_stock = df.groupby("Category")["Stock"].sum()

print("\nStock by Category:")
print(category_stock)

# Chart
plt.bar(category_stock.index, category_stock.values)

plt.title("Stock by Category")
plt.xlabel("Category")
plt.ylabel("Total Stock")

plt.show()