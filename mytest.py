def whenQuest():
    print("Введите количество посетителей: ")
    try:
        quantityQuest = int(input(">"))
        return quantityQuest
    except:
        print("Введите число: ")
        return whenQuest()
################################################33
def whoThisName():
    print("Введи имена приглашенных: ")
    try:
        nameQuest = int(input(">"))
        return nameQuest
    except :
        print("Введите число: ")
        return whoThisName()

def rangeArr():
    print('ww')

def selectVarint():
    try:
        viborVarianta = int(input('>'))
        return viborVarianta
    except:
        print("Введите число")
        return selectVarint()


def __main__():
    quantityQuest = whenQuest()
    quantityPar = quantityQuest
    #print(quantityQuest)
    #nameQuest = whoThisName()
    print("Введите имена")
    arrName = []
    i = 0
    while (i < quantityPar):
        nameMe = input('>')
        arrName.append(nameMe)
        i = i + 1
    print("Показать список приглашенных? ")
    print('1.yes \n2.No')
    varianT = selectVarint()
    if(varianT == 1):
        print("Вы пригласили: ")
        i = 0  
        while(i < len(arrName)):
            print(arrName[i])
            i += 1

    else:
        
    

        
    
    


__main__()