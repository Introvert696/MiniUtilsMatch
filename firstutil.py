from math import *

print("Выберете что вам нужно")
print("1.Простое вычисление")
print("2.Разные формулы") #Допилить другие функции
vvod = int(input("\n>"))
if(vvod == 1):
    print("It's work")
    num_1 = int(input("Введите пераое число: >"))
    num_2 = int(input("Введите второе число: >"))
    print("Что с ними сделать: ")
    print("1.Сложить \n2.Отнять \n3.Разделить \n4.Умножить")
    vvod = int(input("> "))
    if(vvod == 1):                  #НАЧАЛО Все операции
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
        print("Netu")                   #КОНЕЦ Все операции
elif(vvod == 2):
    #print("В разработке")
    print('Выберете что вам нужно: ')
    print("1.Теорема пифагора \n2.Логарифм \n3.Площадь 4-х угольника \n5.Площадь круга\n")
    vvod1 = int(input("> "))
    if (vvod1 == 1):
        print('Введите 2 стороны прямоугольного стреугольника\n')
        a = int(input('a = \n'))
        b = int(input('b = '))
        cen = float(sqrt(a**2 + b**2))
        c = str(cen)
        print("Результат: ",c) 
    elif (vvod1 == 2):
        print('Saglushka')
    elif (vvod1 == 3):
        print('Saglushka')
    elif (vvod1 == 4):
        print('Saglushka')
    elif (vvod1 == 5):
        print('Saglushka')
    else:
        print("Нету такого ответа")
else:
    print("Not working")