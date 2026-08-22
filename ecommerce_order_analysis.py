import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("ecommerce_orders.csv")

print("Order Data:")
print(df)

# Total orders
total_orders = len(df)

# Delivered orders
delivered = df[df["Status"] == "Delivered"]

# Cancelled orders
cancelled = df[df["Status"] == "Cancelled"]

# KPIs
total_revenue = delivered["Order_Value"].sum()
delivery_rate = (len(delivered) / total_orders) * 100
cancellation_rate = (len(cancelled) / total_orders) * 100
average_delivery = delivered["Delivery_Days"].mean()

print("\n--- E-commerce KPIs ---")
print("Total Orders:", total_orders)
print("Delivered Orders:", len(delivered))
print("Cancelled Orders:", len(cancelled))
print("Total Revenue:", total_revenue)
print("Delivery Rate:", round(delivery_rate, 2), "%")
print("Cancellation Rate:", round(cancellation_rate, 2), "%")
print("Average Delivery Days:", round(average_delivery, 2))

# Category-wise revenue
category_revenue = delivered.groupby("Category")["Order_Value"].sum()

print("\nRevenue by Category:")
print(category_revenue)

# Dashboard
plt.figure(figsize=(10, 4))

# Revenue by category
plt.subplot(1, 2, 1)
plt.bar(category_revenue.index, category_revenue.values)
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")

# Order status
plt.subplot(1, 2, 2)
status_count = df["Status"].value_counts()
plt.bar(status_count.index, status_count.values)
plt.title("Order Status")
plt.xlabel("Status")
plt.ylabel("Number of Orders")

plt.tight_layout()
plt.show()