import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("students.csv")

# Plot marks
plt.bar(df["Name"], df["Marks"])

plt.title("Student Marks Analysis")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()