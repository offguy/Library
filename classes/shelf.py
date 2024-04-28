from .book import Book

class Shelf:
    def __init__(self, name=''):
        self.name = name
        self.books_on_shelf = []
        self.is_shelf_full = False
        

    def add_book(self, author, title, num_of_pages):
        if len(self.books_on_shelf) < 5:
            self.books_on_shelf.append(Book(author, title, num_of_pages))
            return "Book added to shelf"
        else:
            self.is_shelf_full = True
            return "No more space on the shelf"
        
    def replace_books(self, replace1, replace2):
        if replace1 > replace2:
            big = replace1
            small = replace2
        elif replace1 < replace2:
            big = replace2
            small = replace1
        else:
            return "same book selected..."
        hold1 = self.books_on_shelf.pop(big)
        hold2 = self.books_on_shelf.pop(small)
        self.books_on_shelf.insert(small, hold1)
        self.books_on_shelf.insert(big, hold2)
        return "books replaced"

    def orgenize_books_by_pages(self):
        sorted(self.books_on_shelf, key=lambda x: x.num_of_pages)
        return "books sorted by number of pages"

