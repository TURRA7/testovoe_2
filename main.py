"""Исполняющий файл проекта."""
import asyncio
from library_tools.library import Library


async def main() -> None:
    library = Library()
    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Поиск книги")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выход")

        choice = input("Выберите действие")

        if choice == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            try:
                year = input("Введите год выпуска книги: ")
                result = await library.add_book(title=title,
                                                author=author,
                                                year=year)
                print(result)
            except ValueError:
                print("Год издания должен быть числом!")

        elif choice == "2":
            try:
                book_id = int(input("Введите id книги для удаления: "))
                result = await library.delete_book(book_id=book_id)
                print(result)
            except ValueError:
                print("id должен быть числом!")

        elif choice == "3":
            field = input("Введите поле поиска: title/author/year: ")
            query = input("Введите значение для поиска: ")
            try:
                result = await library.search_books(query=query, field=field)
                if result and isinstance(result, list):
                    for book in result:
                        print(
                            f"id: {book.id}, Название: {book.title}, Автор: {book.author}, Год: {book.year}, Статус: {book.status}"
                            )
                else:
                    print("Книги не найдены!")
            except ValueError as ex:
                print(ex)

        elif choice == "4":
            result = await library.get_all_books()
            if isinstance(result, list):
                for book in result:
                    print(book)
            else:
                print(result)

        elif choice == "5":
            try:
                book_id = int(input("Введите id книги: "))
                status = input("Введите статус: 'в наличии' или 'выдана'.")
                result = await library.update_status(book_id=book_id,
                                                     status=status)
                print(result)
            except ValueError:
                print("id должен быть числом!")

        elif choice == "6":
            print("Выход из программы.")
            break

        else:
            print("Нет такого действия, повторите выбор!")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as ex:
        print(ex)
