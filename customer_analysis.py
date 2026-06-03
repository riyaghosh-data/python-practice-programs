import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("customer_purchases.csv")

print("Dataset:")
print(df)

# Category-wise spending
category_sales = df.groupby("Category")["Amount"].sum()

print("\nCategory-wise Spending:")
print(category_sales)

# Highest spending category
top_category = category_sales.idxmax()

print("\nHighest Spending Category:", top_category)

# Visualization
plt.figure(figsize=(8,5))
plt.bar(category_sales.index, category_sales.values)

plt.title("Category-wise Customer Spending")
plt.xlabel("Category")
plt.ylabel("Total Amount")

plt.show()