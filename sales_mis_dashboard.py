import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("sales_mis.csv")

# Calculate achievement percentage
df["Achievement (%)"] = (df["Sales"] / df["Target"]) * 100

print(df)

# -----------------------------
# KPI calculations
# -----------------------------

total_sales = df["Sales"].sum()
total_target = df["Target"].sum()
total_orders = df["Orders"].sum()

achievement = (total_sales / total_target) * 100

print("\n----- MIS REPORT -----")
print("Total Sales:", total_sales)
print("Total Target:", total_target)
print("Total Orders:", total_orders)
print("Overall Achievement:", round(achievement, 2), "%")

# -----------------------------
# Region-wise sales
# -----------------------------

region_sales = df.groupby("Region")["Sales"].sum()

print("\nSales by Region:")
print(region_sales)

# -----------------------------
# Product-wise sales
# -----------------------------

product_sales = df.groupby("Product")["Sales"].sum()

print("\nSales by Product:")
print(product_sales)

# Best region
best_region = region_sales.idxmax()

# Best product
best_product = product_sales.idxmax()

print("\nBest Region:", best_region)
print("Best Product:", best_product)

# -----------------------------
# Dashboard
# -----------------------------

plt.figure(figsize=(12, 5))

# Region chart
plt.subplot(1, 2, 1)

plt.bar(region_sales.index, region_sales.values)

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")

# Product chart
plt.subplot(1, 2, 2)

plt.bar(product_sales.index, product_sales.values)

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.tight_layout()
plt.show()