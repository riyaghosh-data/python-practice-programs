import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("customer_orders.csv")

# Calculate Total Amount
df["Total"] = df["Quantity"] * df["Price"]

print(df)

# Product-wise revenue
revenue = df.groupby("Product")["Total"].sum()

print("\nRevenue by Product:")
print(revenue)

# Highest revenue product
top_product = revenue.idxmax()
print("\nHighest Revenue Product:", top_product)

# Visualization
plt.figure(figsize=(8,5))
plt.bar(revenue.index, revenue.values)

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")

plt.tight_layout()
plt.show()