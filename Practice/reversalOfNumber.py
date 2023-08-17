a = 12345

b = str(a)
print(b[::-1])

#without assuming string
reverse = 0
while a>0:
    c = a%10
    reverse = reverse*10 + c
    a = a // 10

print(reverse)