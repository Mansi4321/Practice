class Calculator1:
    num = 100    #Class variable

    def __init__(self, a, b):
        self.firstnum = a
        self.secondnum = b
        print("I am called automatically")


    def summation(self):
        return self.firstnum + self.secondnum


    def subtraction(self):
        if self.firstnum >= self.secondnum:
            return self.firstnum - self.secondnum
        else:
            return self.secondnum - self.firstnum


# obj = Calculator1(11, 10)
#
# print(obj.summation())
#
# print(obj.subtraction())