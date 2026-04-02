# Student Marks Analysis

marks = [78, 85, 62, 90, 55, 88]

# Average marks
average = sum(marks) / len(marks)
print("Average Marks:", average)

# Highest marks
print("Highest Marks:", max(marks))

# Lowest marks
print("Lowest Marks:", min(marks))

# Students who passed (> 60)
passed = [m for m in marks if m > 60]
print("Passed Students:", passed)