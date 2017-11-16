import json


#Конмда 1: загрузить базу данных
#Команда 2: выписать всю информацю о книгах

while(True):
    print("Введите команду")
    command = input()
    if command == "start":
        json_data = open("C:\\Users\\User\\PycharmProjects\\untitled\\books.json")  # Загружаем файл
        d = json.load(json_data)
        listOfbooks = d["book"]
    elif command == "print all":
        for l in listOfbooks:# l - это буква эль
            print("Инфо о книге")
            print("Имя книги: ", l["name"])
            print("Автор: ", l["author"])
            print("Год издания: ", l["year"])
            print("\n")
    elif command == "add book":
        print("add book")
    elif command == "delete book":
        print("""Выберите какую книгу удалять: 
                По названию: by name
                По id: by id
                Последнюю: last""")
        while(True):
            print(">> By")
            typeOfDelete = input()
            if typeOfDelete == "by name":
                print("Введите имя книги")
                name = input()
                i = 0
                for ld in listOfbooks:
                    print("шаг поиска ", i)
                    if ld["name"] == name:
                        print("Нашли нужную кнгиу")
                        print(ld["author"], ld["year"])
                        #listOfbooks.remove(i)
                    i+=1
                #Код который удалает книгу по имени
                break;
            elif typeOfDelete == "by id":
                id = input()
                #Код, который удаляет книгу по id
                break;
            elif typeOfDelete == "last":
                print("last")
                #Код, который удаляет последнюю книгу
                break;
            else:
                print("Нет такой команды для удаления книги. попробуйте еще раз")
        print("Кинга удалена")
        #удалить по имени книги
        #удалить по id книги
        #удалить последнюю добавленную книгу
    elif command == "find":
        print("find book")
    else :
        print("Нет такой команды")




