import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales_forecast.csv")

# Calculate monthly increase
growth = df["Sales"].diff().mean()

# Forecast next month
forecast = df["Sales"].iloc[-1] + growth

print("Average Monthly Growth:", growth)
print("Forecasted Sales for Next Month:", forecast)

# Visualization
plt.plot(df["Month"], df["Sales"], marker="o", label="Actual Sales")

plt.axhline(y=forecast, linestyle="--", label="Forecast")

plt.title("Sales Trend and Forecast")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()

plt.show()