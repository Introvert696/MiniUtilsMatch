from tkinter import *

root = Tk() #Создается окно
rootTextArea = Entry(root, width="20")  #Textarea
rootButtons = Button(root, text="Ssend")
rootLabel = Label(root, bg='black', fg="white", width=20)
##################################################################################
def strToSort(event):
    getText = rootTextArea.get()        #Получение с поля ввода
    getText = getText.split()               # склеивание всего
    getText.sort()                      #сортировка
    rootLabel['text'] = ' '.join(getText)

rootButtons.bind('<Button-1>', strToSort)

##################################################################################
rootTextArea.pack()
rootButtons.pack()
rootLabel.pack()
root.mainloop()
