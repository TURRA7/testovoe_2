"""Модуль для работы с библиотекой."""
import logging


logger = logging.getLogger(__name__)


class LibraryTest:
    """Класс для работы с библиотекой книг."""
    @staticmethod
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

    @staticmethod
    def delete_book(book_id: int) -> str:
        """
        Удаление книги из баблиотеки.

        Args:
            book_id: ID книги в библиотеке.

        Returns:
            ...
        """
        ...

    @staticmethod
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

    @staticmethod
    def get_all_books() -> list[dict]:
        """
        Получение всех книг из библиотеки.

        Returns:
            ...
        """
        ...

    @staticmethod
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
