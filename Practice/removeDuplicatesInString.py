"""
Write a program to remove duplicate characters from a string

"""
#1
str1 = input("Please enter a string:\t")
str = str1.lower()      #In case interviewer wants to remove duplicate letters in uppercase and lowercase
#
def uniquestr(li):
    x = []
    for i in li:
        if i not in x:
            x.append(i)
    return x

def uniqueinorder(li):
    x = []
    for i in li:
        if len(x) == 0 or i != x[-1]:
            x.append(i)
    return x

def listtostring(list):
    str = ""
    return str.join(list)

def stringtolist(string1):
    li = ""
    return li.join(string1)

uniqueString = listtostring(uniquestr(stringtolist(str)))
uniqueInOrderString = listtostring(uniqueinorder(stringtolist(str)))

print(uniqueString)
print(uniqueInOrderString)

#2
from collections import OrderedDict

def removeDuplicates(s):
    return "".join(dict.fromkeys(s))

print("After Removing Duplicates: ",removeDuplicates(str))


print("After Removing Duplicates: {}".format(removeDuplicates(str)))