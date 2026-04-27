import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("student_performance.csv")

# Basic information
print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

# Add total marks
df["Total"] = df["Maths"] + df["Science"] + df["English"]

# Histogram of total marks
plt.hist(df["Total"], bins=5)
plt.title("Distribution of Total Marks")
plt.xlabel("Total Marks")
plt.ylabel("Number of Students")
plt.show()