import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("sales_data.csv")

# Total sales
total = df["Sales"].sum()

# Top product
top = df.loc[df["Sales"].idxmax()]

print("Total Sales:", total)
print("Top Product:", top["Product"])

# Create multiple plots

plt.figure(figsize=(10,4))

# Bar chart
plt.subplot(1,2,1)
plt.bar(df["Product"], df["Sales"])
plt.title("Sales by Product")

# Pie chart
plt.subplot(1,2,2)
plt.pie(df["Sales"], labels=df["Product"], autopct="%1.1f%%")
plt.title("Sales Distribution")

plt.tight_layout()
plt.show()