"""Модуль для работы с библиотекой."""
import json
from typing import List


BOOKS_FILE = "books.json"


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
    def __init__(self) -> None:
        """Инициализация списка книг и метода загрузки."""
        self.books: List[Book] = []
        self.load_books()

    def load_books(self) -> None:
        """Загружает книги из JSON файла."""
        try:
            with open(BOOKS_FILE, "r", encoding="utf-8") as file:
                data = json.loads(file)
                self.books = [Book.from_dict(book) for book in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.books = []

    def save_books(self) -> None:
        """Сохраняет книги в файл JSON."""
        with open(BOOKS_FILE, "w", encoding="utf-8") as file:
            json.dumps(
                [book.to_dict() for book in self.books],
                file, ensure_ascii=False, indent=4)

    def add_book(self, title: str, author: str, year: int) -> str:
        """
        Добавление книги в библиотеку.

        Args:
            title: Название книги
            author: Автор книги
            year: Год выпуска книги

        Returns:
            Возвращает строку с оповещением,
            об успешном добавлении книги.
        """
        new_id = max([book.id for book in self.books], default=0) + 1
        new_book = Book(
            book_id=new_id, title=title, author=author, year=year)
        self.books.append(new_book)
        self.save_books
        return f"Книга добавленна с id {new_id}."

    def find_by_id(self, book_id: int) -> Book:
        """
        Поиск книги по id.

        Args:
            book_id: ID книги

        Returns:
            Возвращает книгу в виде объекта Book если
            она найдена, иначе None
        """
        return next(
            (book for book in self.books if book.id == book_id), None)

    def delete_book(self, book_id: int) -> str:
        """
        Удаление книги по её id.

        Args:
            book_id: ID книги

        Returns:
            Возвращает строку с удачно/неудачно выполненой операцией.
        """
        book = self.find_by_id(book_id=book_id)
        if book:
            self.books.remove(book)
            self.save_books()
            return f"Книга с id {book_id} удалена!"
        else:
            return f"Книга с id {book_id} не найдена!"

    def search_books(self, query: str, field: str) -> Book:
        """
        Поиск книги по названию, автору или году.

        Args:
            query: Значение для поиска
            field: Поле по которому нужно искать книгу

        Returns:
            Возвращает список книг, соответствующий запросу
        """
        if field not in {"title", "author", "year"}:
            raise ValueError("Некорректное поле для поиска!")

        return [
            book for book in self.books if query.lower() in str(
                getattr(book, field)).lower
        ]

    def get_all_books(self) -> list[str] | str:
        """
        Отображение всех книг из библиотеки.

        Returns:
            Если в библиотеке есть книги - возвращает список готовых
            строк-представлений, содержащих: название, автора, год выпуска
            и статус книги, если библиотека пуста, возвращает строку
            с оповещением об этом
        """
        if not self.books:
            return "Библиотека не содержит книги!"
        else:
            books_all = []
            for book in self.books:
                books_all.append(
                    f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, Год: {book.year}, Статус: {book.status}"
                )
            return books_all
