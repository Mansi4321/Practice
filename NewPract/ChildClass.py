from ParentClass import Calculator1


class Calculator2(Calculator1):
    num2 = 200

    def __init__(self,a,b):
        Calculator1.__init__(self, a,b)

    def multiply(self):
        return self.firstnum * self.secondnum

    def division(self):
        if self.firstnum != 0 and self.secondnum != 0:
            return self.firstnum / self.secondnum

    def summation1(self):
        return self.num + self.num2




obj1 = Calculator2(11,10)
print(obj1.multiply())
print(obj1.division())
print(obj1.summation1())
print(obj1.subtraction())

print(issubclass(Calculator1, Calculator2))