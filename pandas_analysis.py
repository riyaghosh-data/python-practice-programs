import pandas as pd

# Load data
df = pd.read_csv("students.csv")

# Show data
print("Dataset:\n", df)

# Basic analysis
print("\nAverage Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())

# Filter students who passed
passed = df[df["Marks"] > 60]
print("\nPassed Students:\n", passed)