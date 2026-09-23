import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("customer_churn.csv")

print(df)

# Total customers
total_customers = len(df)

# Churned customers
churned = df[df["Churn"] == "Yes"]

# Calculate churn rate
churn_rate = (len(churned) / total_customers) * 100

print("\n--- Customer Churn Report ---")
print("Total Customers:", total_customers)
print("Churned Customers:", len(churned))
print("Churn Rate:", round(churn_rate, 2), "%")

# Churn by plan
churn_by_plan = df.groupby("Plan")["Churn"].apply(
    lambda x: (x == "Yes").sum()
)

print("\nChurned Customers by Plan:")
print(churn_by_plan)

# Average monthly charge
avg_charge = df.groupby("Churn")["Monthly_Charges"].mean()

print("\nAverage Monthly Charges:")
print(avg_charge)

# Visualization
plt.figure(figsize=(10, 4))

# Churn count
plt.subplot(1, 2, 1)

churn_count = df["Churn"].value_counts()

plt.bar(churn_count.index, churn_count.values)

plt.title("Customer Churn")
plt.xlabel("Churn Status")
plt.ylabel("Number of Customers")

# Churn by plan
plt.subplot(1, 2, 2)

plt.bar(churn_by_plan.index, churn_by_plan.values)

plt.title("Churn by Plan")
plt.xlabel("Plan")
plt.ylabel("Churned Customers")

plt.tight_layout()
plt.show()