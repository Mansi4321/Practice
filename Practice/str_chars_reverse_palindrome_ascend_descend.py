strToReverse = input("Please enter a string to reverse:\t")

def reverse_string(arg):
    x = ""
    for i in range(len(arg)):
        x = x + arg[len(arg) - i - 1]  #-1 is used because indexes start with 0
    return x

def filtered_string(stringToFilter):
    return ''.join(a.lower() for a in stringToFilter if a.isalnum())

def Alpabetical_order(string):
    return ''.join(a for a in sorted(string) if a.isalnum())

def descending_Alphabetical_order(string):
    return ''.join(a for a in sorted(string, reverse=True) if a.isalnum())

def isPalindrome(strToReverse, strToCheck):
    if filtered_string(strToReverse) == filtered_string(strToCheck):
        return True
    else:
        return False

def remove_duplicates(string):
    str = []
    for i in string:
        if i not in str:
            str.append(i)
    return ''.join(str)


# print(filtered_string)

strToCheck = reverse_string(strToReverse)

print("Reverse of the given string is :{} \t".format(strToCheck))

if isPalindrome(strToReverse, strToCheck) == True:
    print("Given string is a palindrome")
else:
    print("Given string is not a palindrome")

# Ascending_string = remove_duplicates(Alpabetical_order(strToCheck))       #this could be used to remove duplicates

Ascending_string = Alpabetical_order(strToCheck)

print("These are letters in Ascending order:\t{}".format(Ascending_string))

Descending_string = descending_Alphabetical_order(strToCheck)

print("These are letters in descending order:\t{}".format(Descending_string))