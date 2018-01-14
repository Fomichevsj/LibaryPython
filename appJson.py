import json
from Helpers.HelpOperations import delete, add, printAll, saveBooks, find, count, update, findComplex, hardfind


def run(command, listOfbooks, params):
        json_data = open("C:\\Users\\Nic\\Desktop\\DDZ\\ProjRelease2\\LibaryPython\\SolutionFromNet\\books.json")  # Загружаем файл
        d = json.load(json_data)
        listOfbooks = d["books"]
        print("Поступившая комманда: ", command)
        if command == "print all" or command == "1":
            msg = printAll(listOfbooks) # Напечатать информацию о книге
            return msg
        elif command == "add":
            print('Добавим книггу')
            listOfbooks = add(listOfbooks, params)#Добавить книгу. Для описания функции. Смотреть соответствующий файл
            saveBooks(listOfbooks)
            return "add completed. Input print all to see."
        elif command == "delete":
            msg = delete(listOfbooks, params)#Удалить книгу. Для описание функции. Смотреть соответсвующий файл
            return msg
        elif command == "find":
            print("appJson: find book")
            msg = findComplex(listOfbooks, params)# Найти книгу по имени
            return msg
        elif command == "save" or command == "8":
            saveBooks(listOfbooks)# Сохранить изменения в книгах
            return "save completed"
        elif command == "exit":
            print("appJson: Завершаю программу")
            saveBooks(listOfbooks)
            return listOfbooks
        elif command == "hardfind":
            print("appJson: Строгий поиск")
            msg = hardfind(listOfbooks, params)
            return msg
        elif command == "update":
            msg = update(listOfbooks, params)
            return msg
        elif command == "count" or command == "7":
            cnt = count(listOfbooks)
            return cnt
        else :
            print("appJson: Нет такой команды")
            return "no such command"


