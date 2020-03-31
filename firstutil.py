from math import *

print("Выберете что вам нужно")
print("1.Простое вычисление")
print("2.Вычисления производной") #Допилить другие функции
vvod = int(input("\n>"))
if(vvod == 1):
    print("It's work")
    num_1 = int(input("Введите пераое число: >"))
    num_2 = int(input("Введите второе число: >"))
    print("Что с ними сделать: ")
    print("1.Сложить \n2.Отнять \n3.Разделить \n4.Умножить")
    vvod = int(input("> "))
    if(vvod == 1):
        otvet = num_1 + num_2
        print(otvet)
    elif (vvod == 2):
        otvet = num_1 - num_2
        print(otvet)
    elif (vvod == 3):
        otvet = num_1 / num_2
        print(otvet)
    elif (vvod == 4):
        otvet = num_1 * num_2
        print(otvet)
    else:
        print("Netu")
elif(vvod == 2):
    print("В разработке")
else:
    print("Not working")