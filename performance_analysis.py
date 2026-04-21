import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("student_performance.csv")

# Total marks
df["Total"] = df["Maths"] + df["Science"] + df["English"]

# Top student
top = df.loc[df["Total"].idxmax()]
print("Top Student:", top["Name"])

# Average marks
print("Average Total:", df["Total"].mean())

# Visualization - Total marks
plt.bar(df["Name"], df["Total"])
plt.title("Student Performance Analysis")
plt.xlabel("Students")
plt.ylabel("Total Marks")
plt.show()