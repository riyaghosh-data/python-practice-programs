import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("library_books.csv")

print(df)

# Category-wise borrowed books
books = df.groupby("Book_Category")["Books_Borrowed"].sum()

print("\nBooks Borrowed by Category:")
print(books)

# Most borrowed category
top_category = books.idxmax()
print("\nMost Borrowed Category:", top_category)

# Visualization
plt.figure(figsize=(8,5))
plt.bar(books.index, books.values)

plt.title("Library Book Borrowing Analysis")
plt.xlabel("Book Category")
plt.ylabel("Books Borrowed")

plt.show()