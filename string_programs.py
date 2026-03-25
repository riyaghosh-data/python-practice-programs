# 1. Reverse a String
text = input("Enter text: ")
print("Reversed:", text[::-1])


# 2. Count Vowels
text = input("Enter text: ")
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print("Number of vowels:", count)


# 3. Check Palindrome (Improved)
text = input("Enter text: ")
cleaned = text.replace(" ", "").lower()

if cleaned == cleaned[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")