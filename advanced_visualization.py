import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("students.csv")

# Bar chart
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks Analysis")
plt.xlabel("Students")
plt.ylabel("Marks")

# Highlight average line
avg = df["Marks"].mean()
plt.axhline(avg)

plt.show()

# Insights
print("Average Marks:", avg)
print("Top Performer:", df.loc[df["Marks"].idxmax()]["Name"])
print("Lowest Performer:", df.loc[df["Marks"].idxmin()]["Name"])