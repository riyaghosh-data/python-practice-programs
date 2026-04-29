import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("student_performance.csv")

# Calculate correlation
correlation = df[["Maths", "Science", "English"]].corr()
print("Correlation Matrix:")
print(correlation)

# Visualize correlation matrix
plt.imshow(correlation)
plt.colorbar()

plt.xticks(range(len(correlation.columns)), correlation.columns)
plt.yticks(range(len(correlation.columns)), correlation.columns)

plt.title("Subject Correlation Matrix")
plt.show()