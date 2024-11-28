"""Модуль для работы с библиотекой."""
import logging


logger = logging.getLogger(__name__)


class Book:
    """Класс для представления книги."""
    def __init__(self, book_id: int, title: str,
                 author: str, year: int, status: str = "в наличии") -> None:
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self) -> dict:
        """Возвращает словарь с данными книги."""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }

    @staticmethod
    def from_dict(data: dict) -> "Book":
        """Создаст экземпляр Book из словаря."""
        return Book(
            book_id=data['id'],
            title=data['title'],
            author=data['author'],
            year=data['year'],
            status=data['status'],
        )


class Library:
    """Класс для работы с библиотекой книг."""
    # Переделать!!!
    def add_book(title: str, author: str, year: int) -> dict:
        """
        Добавление книги в баблиотеку.

        Args:
            title: Название книги
            author: Автор книги
            year: Год выпуска книги

        Returns:
            ...
        """
        ...

    def delete_book(book_id: int) -> str:
        """
        Удаление книги из баблиотеки.

        Args:
            book_id: ID книги в библиотеке.

        Returns:
            ...
        """
        ...

    def search_book(title: str = None,
                    author: str = None,
                    year: int = None) -> dict:
        """
        Поиск книги в баблиотеке.

        Args:
            title: Название книги
            author: Автор книги
            year: Год выпуска книги

        Returns:
            ...
        """
        ...

    def get_all_books() -> list[dict]:
        """
        Получение всех книг из библиотеки.

        Returns:
            ...
        """
        ...

    def change_status(book_id: int, status: str) -> str:
        """
        Изменение статуса книги в библиотеке.

        Args:
            book_id: ID книги в библиотеке
            status: Новый статус для книги

        Returns:
            ...
        """
        ...
