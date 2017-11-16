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
def add(listOfbooks):
    print("Введите необходимые данные для книги", end="\n")
    print("\tВведите название книги: ", end='')
    name = input()
    print("")
    print("\tВведите автора книги: ", end='')
    author = input()
    print("")
    print("\tВведите год издания книги: ", end='')
    try:
        date = int(input())# TODO нужно учесть, что формат может быть не тот
    except ValueError:
        print("Дата может быть только числом. Попробуйте заново.")
        return
    print()
    print("\tВведите издательский дом: ", end='')
    publis_house = input()
    print()
    listOfbooks.append({
        "id": 0,  # Это нужно будет исправить TODO Исправить это
        "name": name,
        "publish home": publis_house,
        "author": author,
        "year": date
    })
    print("Список книг после изменения: ", listOfbooks)
def printAll(listOfbooks):
    for l in listOfbooks:  # l - это буква эль
        print("Инфо о книге")
        print("Имя книги: ", l["name"])
        print("Автор: ", l["author"])
        print("Год издания: ", l["year"])
        print("\n")
def saveBooks(listOfbooks):
    print("Тип listOfBooks = ", type(listOfbooks))
    print("Список книг теперь такой:\n", listOfbooks)
    data = {}
    data['books'] = listOfbooks
    with open('books.json', 'w') as outfile:
        json.dump(data, outfile)