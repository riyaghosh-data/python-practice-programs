import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("employee_salary.csv")

# Average salary by department
dept_salary = df.groupby("Department")["Salary"].mean()

# Dashboard
plt.figure(figsize=(10,4))

# Bar Chart
plt.subplot(1,2,1)
plt.bar(dept_salary.index, dept_salary.values)
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Salary")

# Pie Chart
plt.subplot(1,2,2)
plt.pie(
    df["Department"].value_counts(),
    labels=df["Department"].value_counts().index,
    autopct="%1.1f%%"
)
plt.title("Employee Distribution")

plt.tight_layout()
plt.show()

print("\nAverage Salary by Department:")
print(dept_salary)

highest_paid = df.loc[df["Salary"].idxmax()]
print("\nHighest Paid Employee:")
print(highest_paid)