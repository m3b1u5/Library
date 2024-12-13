# ДЗ: Создание словаря библиотеки

Задание: 

В ближайших заданиях вы будете реализовывать программу по управлению небольшой библиотекой книг. В библиотеке будут храниться следующие данные о книгах: название, автор, год издания и наличие книги (в наличии или выдана). В дальнейшем функционал к программе будет добавляться поэтапно.

Требование:

Создайте словарь library, где ключами будут названия книг, а значениями — словари с информацией о книге (автор, год издания, наличие).  После этого реализуйте первую функцию 'book_list_view(library)', которая выводит в консоль названия всех книг в библиотеке. Если в библиотеке нет книг, функция выводит сообщение об этом.

Требование:

   - Реализуйте функцию `add_book(title, author, year)`, которая добавляет книгу в словарь `library`. Поле `наличие` при добавлении новой книги должно быть `None` (означает, что книга в библиотеке, но не определен ее статус).

   - Если книга с таким названием уже существует, программа должна предложить обновить информацию о ней.

   - Функция должна вывести сообщение об успешном добавлении/обновлении информации о книге с ее названием

Требование:

   - Реализуйте функцию `remove_book(title)`, которая удаляет книгу из словаря. Если книга не найдена, программа должна вывести сообщение об этом.

   - После удаления функция должна вывести сообщение об удалении книги с ее названием.

Требование:

   - Реализуйте функцию `issue_book(title)`, которая отмечает книгу как выданную (`наличие` становится `False`).

   - Реализуйте функцию `return_book(title)`, которая отмечает книгу как вернувшуюся в библиотеку (`наличие` становится `True`).

Требование:

   - Реализуйте функцию `find_book(title)`, которая выводит информацию о книге по ее названию. Если книга не найдена, должно выводиться соответствующее сообщение.