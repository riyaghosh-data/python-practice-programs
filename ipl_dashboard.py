import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("ipl_team_performance.csv")

# Win percentage
df["Win_Percentage"] = (df["Wins"] / df["Matches"]) * 100

print(df)

plt.figure(figsize=(10,4))

# Bar Chart
plt.subplot(1,2,1)
plt.bar(df["Team"], df["Wins"])
plt.title("IPL Team Wins")
plt.xticks(rotation=45)

# Pie Chart
plt.subplot(1,2,2)
plt.pie(
    df["Wins"],
    labels=df["Team"],
    autopct="%1.1f%%"
)
plt.title("Win Distribution")

plt.tight_layout()
plt.show()