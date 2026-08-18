import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("monthly_sales.csv")

# Calculate return rate
df["Return_Rate"] = (df["Returns"] / df["Orders"]) * 100

print("Sales Data:")
print(df)

# Monthly revenue
monthly_revenue = df.groupby("Month")["Revenue"].sum()

print("\nMonthly Revenue:")
print(monthly_revenue)

# Category revenue
category_revenue = df.groupby("Category")["Revenue"].sum()

print("\nCategory Revenue:")
print(category_revenue)

# Total KPIs
total_orders = df["Orders"].sum()
total_revenue = df["Revenue"].sum()
total_returns = df["Returns"].sum()

print("\n--- MIS KPIs ---")
print("Total Orders:", total_orders)
print("Total Revenue:", total_revenue)
print("Total Returns:", total_returns)

# Best category
best_category = category_revenue.idxmax()

print("Best Revenue Category:", best_category)

# Charts
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.bar(monthly_revenue.index, monthly_revenue.values)
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)

plt.subplot(1, 2, 2)
plt.bar(category_revenue.index, category_revenue.values)
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")

plt.tight_layout()
plt.show()