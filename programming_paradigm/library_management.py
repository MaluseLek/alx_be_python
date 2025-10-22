class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)
        else:
            raise ValueError("Invalid: Only Book instances can be added.")
        
    def check_out_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.check_out():
                    return f"{book.title} has been checked out."
                else:
                    return f"{book.title} is already checked out."
        return f"Book '{title}' not found in the library"

    def return_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.return_book():
                    return f"{book.title} has been returned."
                else:
                    return f"{book.title} is already in the library."
        return f"Book '{title}' not found in the library"


    def list_available_books(self):
        available_books = [book.title for book in self._books if not book._is_checked_out]
        if available_books:
            for book in available_books:
                print(f"- {book}")
        else:
            print("No books are currently available in the library.")
    
    