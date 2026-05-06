import pandas as pd

# Load data
df = pd.read_csv("students_performance.csv")

# Group by section
group_avg = df.groupby("Section")[["Maths", "Science", "English"]].mean()

print("Average Marks by Section:\n")
print(group_avg)