# ДЗ: Создание словаря библиотеки


def book_list_view(library):
    if not library:
        print("Библиотека пуста")
    else:
        print("Список книг по названию:\n" + '_' * 50)
        for book in library:
            print(book)
        print('_' * 50)


def main():
    library = {
        "Python для чайников": {"author": "Алексей Рыбицкий", "year": 2024, "present": True},
        "Словарь": {"author": "КиМ", "year": 998, "present": False},
        "Красненькая такая": {"author": "Автор", "year": 1, "present": True},
    }

    book_list_view(library)


main()
