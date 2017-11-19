import json
#Файл реализует нужные функции для удалени, добавления, поиска книг в библиотеке
def delete(listOfbooks):
    print("""Выберите какую книгу удалять: 
            По названию: by name
            По id: by id
            Последнюю: last""")
    while (True):
        print(">> By")
        typeOfDelete = input()
        if typeOfDelete == "by name":
            print("Введите имя книги")
            name = input()
            i = 0
            found = False
            for ld in listOfbooks:
                print("шаг поиска ", i)
                if ld["name"] == name:
                    print("Нашли нужную кнгиу")
                    print(ld["author"], ld["year"])
                    print(ld)
                    print(listOfbooks)
                    print("i = ", i)
                    found = True
                    break
                i += 1
            if found:
                print("Элемент для удаления. Значение i здесь  = ", i)
                print(listOfbooks.pop(i))
                print("Кинга удалена")
            else:
                print("Такой эелемент не найден. Попробуйте еще раз")
            break
        elif typeOfDelete == "by id":
            id = input()
            # Код, который удаляет книгу по id
            break
        elif typeOfDelete == "last":
            print("last")
            # Код, который удаляет последнюю книгу
            break
        else:
            print("Нет такой команды для удаления книги. попробуйте еще раз")
            break
    # удалить по имени книги
    # удалить по id книги
    # удалить последнюю добавленную книгу
def add(listOfbooks, params):
    params = params.split(" ")
    print(params)
    print("p1 ", params[0])
    print("p2 ", params[1])
    print("p3", params[2])
    print("p4", params[3])
    listOfbooks.append({
        "id": 0,  # Это нужно будет исправить TODO Исправить это
        "name": params[0],
        "publish home": params[3],
        "author": params[1],
        "year": int(params[2])
    })
    print("Список книг после изменения: ", listOfbooks)
    return listOfbooks
def printAll(listOfbooks):
    res = ""
    for l in listOfbooks:  # l - это буква эль
        print("Инфо о книге")
        print("Имя книги: ", l["name"])
        print("Автор: ", l["author"])
        print("Год издания: ", l["year"])
        print("\n")
        res = res +"Инфо о книге:\n" + "Имя книги: " + str(l["name"]) + "\nАвтор: " + str(l["author"]) +"\nГод издания: " + str(l["year"])
    print("будет возращать сообщение: ", res)
    return res
def saveBooks(listOfbooks):
    print("Тип listOfBooks = ", type(listOfbooks))
    print("Список книг теперь такой:\n", listOfbooks)
    data = {}
    data['books'] = listOfbooks
    with open('books.json', 'w') as outfile:
        json.dump(data, outfile)