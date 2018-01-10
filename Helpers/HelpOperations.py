import json
#Файл реализует нужные функции для удалени, добавления, поиска книг в библиотеке
import time


def delete(listOfbooks, params):
    i = 0
    found = False
    for ld in listOfbooks:
        print("шаг поиска ", i)
        if ld["name"] == params:
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
        saveBooks(listOfbooks)
        return "success delete"
    else:
        print("Такой эелемент не найден. Попробуйте еще раз")
        return "no such element"

#Подсчет числа элементов книг в библиотеке
def count(listOfbooks):
    return len(listOfbooks)
    print(len(listOfbooks))

def find(listOfbooks, params):
    i = 0
    found = False
    for ld in listOfbooks:
        print("шаг поиска ", i)
        if ld["name"] == params:
            print("Нашли нужную кнгиу")
            print(ld["author"], ld["year"])
            print(ld)
            print(listOfbooks)
            print("i = ", i)
            found = True
            break
        i += 1
    if found:
        print("Нашли нашу книгу. Значение i здесь  = ", i)
        res = "Книга найдена\n" + "Название: " + ld["name"] + "\nАвтор: " + ld["author"] \
              + "\nГод издания: " + str(ld["year"]) + "\nИздательский дом: " + ld["publish home"] + "\n"
        return res
    else:
        print("Такой эелемент не найден. Попробуйте еще раз")
        return "no such element"

def add(listOfbooks, params):
    params = params.split(" ")
    print(params)
    print("p1 ", params[0])
    print("p2 ", params[1])
    print("p3", params[2])
    print("p4", params[3])
    for i in listOfbooks:
        if i["name"] == params[0] and i["author"] == params[1] and str(i["year"]) == str(params[2]):
            print('Нашли нужную книгу. Увеличим число элементов в эой книге')
            i["count"] = int(i["count"]) + 1
            return listOfbooks
    millis = int(round(time.time() * 1000))
    listOfbooks.append({
        "id": millis,
        "name": params[0],
        "publish home": params[3],
        "author": params[1],
        "year": int(params[2]),
        "count": 1
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
        print("Издатеьский дом: ", l["publish home"])
        print("\n")
        res = res +"Инфо о книге:\n" + "Имя книги: " + str(l["name"]) + "\nАвтор: " + str(l["author"]) \
              +"\nИндетификатор: " + str(l["id"]) + "\nИздательский дом: " + str(l["publish home"]) + "\nКоличество: " + str(l["count"])+ "\nГод: " + str(l["year"]) + "" +"\n\n"
    print("будет возращать сообщение: ", res)
    return res
def saveBooks(listOfbooks):
    print("Тип listOfBooks = ", type(listOfbooks))
    print("Список книг теперь такой:\n", listOfbooks)
    data = {}
    data['books'] = listOfbooks
    with open('/Users/fomichevalexey/PycharmProjects/LibaryPython/SolutionFromNet/books.json', 'w') as outfile:
        json.dump(data, outfile)