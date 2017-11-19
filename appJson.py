import json
from Helpers.HelpOperations import delete, add, printAll, saveBooks


def run(command, listOfbooks):
    #while(True):
        #print("Введите команду")
        #command = input()
        #if command == "start":
        json_data = open("C:\\Users\\User\\PycharmProjects\\untitled\\books.json")  # Загружаем файл
        d = json.load(json_data)
        listOfbooks = d["books"]
        print("Поступившая комманда: ", command)
        if command == "print all":
            printAll(listOfbooks) # Напечатать информацию о книге
        elif command == "add book":
            add(listOfbooks)#Добавить книгу. Для описания функции. Смотреть соответствующий файл

        elif command == "delete book":
            delete(listOfbooks)#Удалить книгу. Для описание функции. Смотреть соответсвующий файл

        elif command == "find":
            print("appJson: find book")
        elif command == "save":
            saveBooks(listOfbooks)# Сохранить изменения в книгах

        elif command == "exit":
            print("appJson: Завершаю программу")
            return listOfbooks
        else :
            print("appJson: Нет такой команды")


