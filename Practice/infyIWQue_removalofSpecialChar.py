a = "Hello$ $Wor$ld"
#output should be without $ and the preceding letter should be removed
# def strToDict(a):
#     return "".join(a)

x = []
for i in a:
    if i != "$":
        x.append(i)
    elif i == "$" and x[-1].isalnum():
        x.remove(x[-1])

print(x)

def dictTostr(b):
    return "".join(b)

str1 = dictTostr(x)

print(str1)