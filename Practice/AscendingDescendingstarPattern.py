''' write a program for the below pattern with only one while loop
*
**
***
****
*****
****
***
**
*
'''
a = 0
bool = True
while(a<=5):
    if a<0:
        break
    elif a >= 5 :
        bool = False
    if(bool) :
                a = a + 1
    else:
                a = a - 1
    print("*"*a)        #Prints *, a times. Suppose a = 2, so print("*"*2), it means * will be printed twice
# print("*"*2)  #We can use this to check above statment