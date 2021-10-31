str = input("Please enter a value to check if Palindrome:\t")

filtered_str = ''.join(a.lower() for a in str if a.isalnum())

# print(filtered_str)

def reverse_str(str):
    x = ''
    for i in range(len(str)):
        x = x + str[len(str)-i-1]
    return x

str_to_check = reverse_str(filtered_str)
# print(str_to_check)

def is_Palindrome(strToCheck, Filtered_str):
    if strToCheck == Filtered_str:
        return True
    else:
        return False

bool = is_Palindrome(str_to_check, filtered_str)

if bool == True:
    print("Given statement is Palindrome")
else:
    print("given statement is not palindrome")