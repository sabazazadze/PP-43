from book import Book
from validators import clean_text, clean_year, normalize

THIN = "-" * 50


class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, year):
        title = clean_text(title, "სათაური")
        author = clean_text(author, "ავტორი")
        year = clean_year(year)

        for book in self.books:
            if normalize(book.title) == normalize(title) and \
               normalize(book.author) == normalize(author):
                raise ValueError("ასეთი წიგნი უკვე არსებობს.")

        book = Book(title, author, year)
        self.books.append(book)
        return book

    def search_book(self, title):
        query = normalize(clean_text(title, "საძიებო სიტყვა"))

        found = []
        for book in self.books:
            if query in normalize(book.title):
                found.append(book)

        if not found:
            print("წიგნი ვერ მოიძებნა")
        else:
            print(f"ნაპოვნია: {len(found)} წიგნი")
            for i, book in enumerate(found, start=1):
                print(f"  {i}. {book}")

        return found

    def remove_book(self, title):
        query = normalize(clean_text(title, "სათაური"))

        for book in self.books:
            if normalize(book.title) == query:
                self.books.remove(book)
                return True
        return False

    def show_books(self):
        if not self.books:
            print("წიგნების სია ცარიელია.")
            return

        print(f"{'#':<4}{'სათაური':<30}{'ავტორი':<20}{'წელი':<6}")
        print(THIN)
        for i, book in enumerate(self.books, start=1):
            print(f"{i:<4}{book.title[:28]:<30}{book.author[:18]:<20}{book.year:<6}")
        print(THIN)
        print(f"სულ: {len(self.books)} წიგნი")
