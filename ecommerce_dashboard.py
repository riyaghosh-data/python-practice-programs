import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("ecommerce_sales.csv")

# Calculate revenue
df["Revenue"] = df["Quantity"] * df["Price"]

print(df)

# Revenue by category
category_revenue = df.groupby("Category")["Revenue"].sum()

# Top product
top_product = df.groupby("Product")["Revenue"].sum().idxmax()

print("\nRevenue by Category:")
print(category_revenue)

print("\nTop Revenue Product:", top_product)

# Dashboard
plt.figure(figsize=(10,4))

# Bar chart
plt.subplot(1,2,1)
plt.bar(category_revenue.index, category_revenue.values)
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")

# Pie chart
plt.subplot(1,2,2)
plt.pie(
    category_revenue.values,
    labels=category_revenue.index,
    autopct="%1.1f%%"
)
plt.title("Revenue Distribution")

plt.tight_layout()
plt.show()