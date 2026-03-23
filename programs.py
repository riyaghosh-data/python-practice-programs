# 1. Palindrome Checker
text = input("Enter a word: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# 2. Numbers greater than 5
numbers = [1, 6, 3, 8, 2, 10]
result = [num for num in numbers if num > 5]
print("Numbers > 5:", result)


# 3. Pattern Printing
n = 3
for i in range(1, n+1):
    print(" " * (n-i) + "0 " * i)