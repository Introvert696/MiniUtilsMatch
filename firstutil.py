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
    print("1.Теорема пифагора \n2.Логарифм \n3.Площадь 4-х угольника \n4.Площадь круга\n")
    vvod1 = int(input("> "))
    if (vvod1 == 1):
        print('Введите 2 стороны прямоугольного треугольника\n')
        a = int(input('a = \n'))
        b = int(input('b = '))
        cen = float(sqrt(a**2 + b**2))
        cen = round(cen, 3)                 #Округление до 3 знаков после точки
        c = str(cen)
        print("Результат: ",c) 
    elif (vvod1 == 2):
        print('Логарифм числа x по основанию y\n')
        x = int(input('Введите x: \n> '))
        y = int(input('Введите y: \n> '))
        resultlog = float(log(x, y))
        relog = str(resultlog)
        print("Result", relog)
    elif (vvod1 == 3):
        print('Площадь 4-х угольника \nДля начала введите ваши 4 стороны')
        a = int(input("Введите 1 сторону: "))
        b = int(input("Введите 2 сторону: "))
        c = int(input("Введите 3 сторону: "))
        d = int(input("Введите 4 сторону: "))
        ploshad = a * b * c * d
        ploshad = str(ploshad)
        print("Результат: ",ploshad)
    elif (vvod1 == 4):
        print('Площадь круга')
        res = int(input("Введите радиус круга: "))
        pis = 3.14
        otvet = float(2 * pis * res)
        otvet = str(otvet)
        print("Радиус приблизительно: ",otvet)
    elif (vvod1 == 5):
        print('пасхалОчка')
    else:
        print("Нету такого ответа")
else:
    print("Not working")