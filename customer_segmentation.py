import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("customer_segmentation.csv")

# Create customer segments
def segment_customer(spending):
    if spending >= 50000:
        return "High Value"
    elif spending >= 20000:
        return "Medium Value"
    else:
        return "Low Value"

df["Segment"] = df["Total_Spending"].apply(segment_customer)

print(df)

# Count customers in each segment
segment_counts = df["Segment"].value_counts()

print("\nCustomer Segments:")
print(segment_counts)

# Visualization
plt.figure(figsize=(7, 5))

plt.bar(segment_counts.index, segment_counts.values)

plt.title("Customer Segmentation")
plt.xlabel("Customer Segment")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.show()