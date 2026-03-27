# 1. Sum of numbers from 1 to n
n = int(input("Enter a number: "))
total = sum(range(1, n+1))
print("Sum:", total)


# 2. Multiplication Table
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num*i)


# 3. Even numbers from list
numbers = [1, 2, 3, 4, 5, 6]
even = [n for n in numbers if n % 2 == 0]
print("Even numbers:", even)