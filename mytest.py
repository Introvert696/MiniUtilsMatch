import random

############################################
"""
wordIAm = ["I ","You ","We ","Me "]
wordNeedThink = ["Need ","Think ","Have "]
wordFood = ["Apple ","Melone ","Cherry"]
a = random.randrange(0,3)
b = random.randrange(0,2)
c = random.randrange(0,2)
print(wordIAm[a],wordNeedThink[b],wordFood[c])
print(a)

def abcd(a,b):
    res = a + b
    return res

print(abcd(2,3))

def test():
    try:
        i = int(input("Number"))
    except (ValueError, TypeError):
        print("Nepravilno")
        return test()
test()
"""

def vibor():
    num_1 = int(input("Введите пераое число: >"))
    num_2 = int(input("Введите второе число: >"))
    return num_1, num_2

print(vibor())
mass = vibor()
num_1 = mass[0]
num_2 = mass[1]
print(num_1,num_2)