import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales_outlier_data.csv")

# Calculate statistics
mean_sales = df["Sales"].mean()
std_sales = df["Sales"].std()

# Detect outliers
outliers = df[df["Sales"] > mean_sales + 2 * std_sales]

print("Average Sales:", mean_sales)
print("\nDetected Outliers:")
print(outliers)

# Visualization
plt.boxplot(df["Sales"])
plt.title("Sales Outlier Detection")
plt.ylabel("Sales")
plt.show()