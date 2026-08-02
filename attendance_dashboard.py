import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("student_attendance.csv")

# Calculate attendance percentage
df["Attendance (%)"] = (df["Classes_Attended"] / df["Classes_Held"]) * 100

print(df)

# Department-wise average attendance
dept_attendance = df.groupby("Department")["Attendance (%)"].mean()

print("\nAverage Attendance by Department:")
print(dept_attendance)

# Dashboard
plt.figure(figsize=(10,4))

# Bar Chart
plt.subplot(1,2,1)
plt.bar(dept_attendance.index, dept_attendance.values)
plt.title("Average Attendance by Department")
plt.xlabel("Department")
plt.ylabel("Attendance (%)")

# Pie Chart
plt.subplot(1,2,2)
plt.pie(
    df["Department"].value_counts(),
    labels=df["Department"].value_counts().index,
    autopct="%1.1f%%"
)
plt.title("Students by Department")

plt.tight_layout()
plt.show()