import random

def randomListCreation(baserange, randrange1, randrange2, randint1, randint2):
    baselist= []
    for i in range(baserange + random.randrange(randrange1, randrange2)):
        num = random.randint(randint1,randint2)
        baselist.append(num)
    return baselist