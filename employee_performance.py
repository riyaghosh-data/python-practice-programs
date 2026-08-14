import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("employee_performance.csv")

# Calculate target achievement
df["Achievement (%)"] = (df["Sales"] / df["Target"]) * 100

# Classify performance
df["Performance"] = df["Achievement (%)"].apply(
    lambda x: "Achieved" if x >= 100 else "Below Target"
)

print(df)

# Department-wise average achievement
dept_performance = df.groupby("Department")["Achievement (%)"].mean()

print("\nAverage Achievement by Department:")
print(dept_performance)

# Best employee
best_employee = df.loc[df["Achievement (%)"].idxmax()]

print("\nBest Performing Employee:")
print(best_employee)

# Visualization
plt.figure(figsize=(9, 5))

plt.bar(
    df["Employee"],
    df["Achievement (%)"]
)

plt.axhline(
    y=100,
    linestyle="--",
    label="Target = 100%"
)

plt.title("Employee Target Achievement")
plt.xlabel("Employee")
plt.ylabel("Achievement (%)")
plt.xticks(rotation=45)
plt.legend()

plt.tight_layout()
plt.show()