""" example to print pattern
1
22
333
4444
"""

#Nested For:
for i in range(1,5):
    for j in range(i):
        print(i, end="")
        """
        end="" is used in order to keep the 2nd result of the nested for loop in the same line. if we don't use end="", the result
        will be printed like below:
        1
        
        2  
        2   In order to keep this 2nd result in the same line, we used end=''
        
        3
        3
        3 and so on.
        """
    print()