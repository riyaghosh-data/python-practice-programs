import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("company_sales.csv")

# Total sales
df["Total"] = df["Online"] + df["Offline"]

print(df)

print("\nAverage Total Sales:", df["Total"].mean())

best_month = df.loc[df["Total"].idxmax()]
print("Best Month:", best_month["Month"])

# Create charts
plt.figure(figsize=(10,4))

# Line chart
plt.subplot(1,2,1)
plt.plot(df["Month"], df["Online"], marker="o", label="Online")
plt.plot(df["Month"], df["Offline"], marker="o", label="Offline")
plt.title("Sales Trend")
plt.legend()

# Pie chart
plt.subplot(1,2,2)
plt.pie(
    [df["Online"].sum(), df["Offline"].sum()],
    labels=["Online","Offline"],
    autopct="%1.1f%%"
)
plt.title("Sales Distribution")

plt.tight_layout()
plt.show()