import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("employee_salary.csv")

# Create new feature
df["Total_Salary"] = df["Hours_Worked"] * df["Hourly_Rate"]

print(df)

# Highest salary employee
top_employee = df.loc[df["Total_Salary"].idxmax()]
print("\nHighest Salary Employee:")
print(top_employee["Name"])

# Visualization
plt.bar(df["Name"], df["Total_Salary"])
plt.title("Employee Total Salary")
plt.xlabel("Employee")
plt.ylabel("Salary")
plt.show()