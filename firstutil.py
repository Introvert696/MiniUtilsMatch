from math import *

############################
def slozhenie(a,b):
    result = a + b
    res = str(result)
    print("Ответ: ", res)
############################
def otnyatie(a,b):
    result = a - b
    res = str(result)
    print("Ответ: ", res)
############################
def raznost(a,b):
    result = a / b
    res = str(result)
    print("Ответ :", res)
############################
def umnozhenie(a,b):
    result = a * b
    res = str(result)
    print("Ответ: ", res)
#############################
def pifagor():
    try:
        a = int(input('a = '))
        b = int(input('b = '))
    except (TypeError,ValueError):
        print("Введите число:")
        return pifagor()
    cen = float(sqrt(a**2 + b**2))
    cen = round(cen, 3)                 #Округление до 3 знаков после точки
    c = str(cen)
    print("Результат: ",c)
    return main()
###############################
def logarifm(x,y):
    resultlog = float(log(x, y))
    resultlog = round(resultlog, 3)
    relog = str(resultlog)
    print("Result", relog)
################################
def ploshad():
    try:
        a = int(input('1я сторона = '))
        b = int(input('2я сторона = '))
        c = int(input('3я сторона = '))
        d = int(input('4я сторона = '))
    except (TypeError,ValueError):
        print("Введите число:")
        return ploshad()
    cen = a * b * c * d
    cen = round(cen, 3)                 #Округление до 3 знаков после точки
    c = str(cen)
    print("Результат: ",c)
    return main()
#################################
def ploshadkrug():
    try:
        res = int(input("Введите радиус круга: "))
    except (TypeError,ValueError):
        print('Введите коректный ответ:')
        return ploshadkrug()
    pis = 3.14
    otvet = float(2 * pis * res)
    otvet = str(otvet)
    print("Радиус приблизительно: ",otvet)
    return main()
##################################
#############################################################################
#############################################################################
"""
==================================
а = Условия выбора
1 - нахождение скорости
2 - нахождения расстояния
3 - нахождения времени
=================================
b = скорость 
с = расстояние
d = время
"""
def skorost(c,d):
    skorost1 = c / d
    print('Ответ: ', skorost1)
    
def rasstoyanie(b,d):
    rstoyanie = b*d
    print('Ответ: ', rstoyanie)

def vremya(c,b):
    vrem = c / b
    print("Ответ", vrem)

#############################################################################
#############################################################################
#############################################################################
def vibor():                                  #Выбор и проверка num_1 и num_2
    try:                                    
        num_1 = int(input("Введите пераое число: >"))
        num_2 = int(input("Введите второе число: >"))
        return num_1, num_2
    except (TypeError,ValueError):
        print('Введите цифры')
        return vibor()
##########################################################################
def oneVibor():             #Выбор 1 значения vvod
    try:
        vvod = int(input("\n>"))
        return vvod
    except (TypeError,ValueError):
        print("Введите число")
        return oneVibor()

####################################################
def main():
    print("Выберете что вам нужно")
    print("1.Простое вычисление")
    print("2.Разные формулы") #Допилить другие функции
    print("3.Выход")
    vvod = oneVibor()
    if(vvod == 1):
        ######################################
        """
        try:
            num_1 = int(input("Введите пераое число: >"))
            num_2 = int(input("Введите второе число: >"))
        except (TypeError,ValueError):
            pass
        """
        ##########################################
        print("Простое вычисление: ")
        massvib = vibor()
        #print(massvib)        просмотр массива
        
        num_1 = massvib[0]
        num_2 = massvib[1]

        print("Что с ними сделать: ")
        print("1.Сложить \n2.Отнять \n3.Разделить \n4.Умножить")
        vvod = oneVibor()
        if(vvod == 1):                  #НАЧАЛО Все операции
            slozhenie(num_1,num_2) 
            return main()         #Сложение
        elif (vvod == 2):
            otnyatie(num_1,num_2)
            return main()
        elif (vvod == 3):
            raznost(num_1,num_2)
            return main()
        elif (vvod == 4):
            umnozhenie(num_1,num_2)
            return main()
        else:
            print("Netu")
            return main()                  #КОНЕЦ Все операции
    elif(vvod == 2):
        print('Выберете что вам нужно: ')
        print("1.Теорема пифагора \n2.Логарифм \n3.Площадь 4-х угольника \n4.Площадь круга\n")
        print("5.Нахожедние скорости/времени/расстояния")
        vvod = oneVibor()
        if (vvod == 1):
            print('Введите 2 стороны прямоугольного треугольника\n') 
            pifagor()
        elif (vvod == 2):
            print('Логарифм числа x по основанию y\n')
            x = int(input('Введите x: \n> '))
            y = int(input('Введите y: \n> '))
            logarifm(x,y)
        elif (vvod == 3):
            print('Площадь 4-х угольника \nДля начала введите ваши 4 стороны')
            ploshad()
            return main()
        elif (vvod == 4):
            print('Площадь круга')
            ploshadkrug()
        elif (vvod == 5):
            print('Выберете что именно: \n1.Скорость\n2.Растояние\n3.Время')
            a = input('>')
            a = int(a)
            if (a == 1):
                print('Нахождение скорости:')
                c = int(input("Введите растояние: > "))
                d = int(input("Введите время: >"))
                skorost(c,d)
            elif(a == 2):
                print('Нахождение Расстояния: ')
                b = int(input("Введите скорость (км/ч): >"))
                d = int(input("Введите время: >"))
                rasstoyanie(b,d)
            elif (a == 3):
                print('Нахождения Времени:')
                c = int(input("Введите растояние: > "))
                b = int(input("Введите скорость (км/ч): >"))
                vremya(c,b)
            else:
                print('Nothing')
        else:
            print("Нету такого ответа")
    elif(vvod == 3):
        print("ПОКА")
    else:
        print("Not working")
        return main()
main()