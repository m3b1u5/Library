# ДЗ: Создание словаря библиотеки


def book_list_view(library):
    if not library:
        print("\nБиблиотека пуста")
    else:
        print("\nСписок книг по названию:\n" + '_' * 50)
        for book in library:
            print(book)
        print('_' * 50 + '\n')


def update_book(title, author, year, library):
    while True:
        try:
            update_required = input("\nКнига уже есть в списке, обновить информацию (Да \ Нет)?: ").lower()
            if update_required == 'да':
                library[title]['author'] = author
                library[title]['year'] = year
                print(f"Информация о книге \"{title}\" обновлена.")
                return
            elif update_required == 'нет':
                print(f"Информация о книге \"{title}\" оставлена без изменений.")
                return
            else:
                raise ValueError
        except ValueError:
            print("Введите Да или Нет.")


def add_book(title, author, year, library):
    if title in library:
        update_book(title, author, year, library)
    else:
        library[title] = {"author": author, "year": year, "present": None}
        print(f"Информация о книге \"{title}\" успешно добавлена в список библиотеки.")


def remove_book(title, library):
    if title not in library:
        print(f"Книга \"{title}\" не найдена в списке библиотеки.")
        return
    else:
        del library[title]
        print(f"Книга \"{title}\" успешно удалена из списка библиотеки.")


def issue_book(title, library):
    if title not in library:
        print(f"Книга \"{title}\" не найдена в списке библиотеки.")
        return
    elif not library[title]["present"]:
        print(f"Книга \"{title}\" уже выдана.")
        return
    else:
        library[title]["present"] = False
        print(f"Книга \"{title}\" успешно выдана.")


def return_book(title, library):
    if title not in library:
        print(f"Книга, \"{title}\" с другой библиотеки, невозможно вернуть ее в список.")
        return
    else:
        library[title]["present"] = True
        print(f"Книга \"{title}\" успешно возвращена.")


def main():
    library = {
        "Python для чайников": {"author": "Алексей Рыбицкий", "year": 2024, "present": True},
        "Словарь": {"author": "КиМ", "year": 998, "present": False},
        "Красненькая такая": {"author": "Автор", "year": 1, "present": True},
    }

    book_list_view(library)
    # add_book('Словарь', 'Я', 1999, library)
    add_book('Вариант Бис', 'Сергей Владимирович Анисимов', 2003, library)
    remove_book('Словарь', library)
    remove_book('Словарь', library)
    book_list_view(library)
    issue_book('Python для чайников', library)
    issue_book('C++ для чайников', library)
    return_book('Python для чайников', library)
    return_book('C++ для чайников', library)


main()