"""
Write a program to reverse a string
"""

def reverse(word):
    x = ""
    for i in range(len(word)):
        x = x + word[len(word)-i-1]
    return x

str1 = input("Please enter a string:\t")

filtered_str = ''.join(i.lower() for i in str1 if i.isalnum())

reversed_str = reverse(filtered_str)

print(reversed_str)

if filtered_str == reversed_str:
    print("This is palindrome")
else:
    print("not a palindrome")