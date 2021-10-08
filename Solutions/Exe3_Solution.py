Nmblist2 = [1,2,3,4,5,6,7,8,9,10]

print([x for x in Nmblist2 if x < 5])

print("Please find the list present:\t{}".format(Nmblist2))
num = int(input("Please enter a number and we will print numbers smaller than it from the list:\t"))

print([x for x in Nmblist2 if x < num])
#print([output for reference in list if condition])