"""Модуль для работы с библиотекой."""
import json
from typing import List, Optional, Union


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
