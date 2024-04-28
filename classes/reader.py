import datetime

class Reader:
    def __init__(self, id):
        self.id = id
        self.books = []

    def read_book(self, title):
        date = datetime.datetime.now().date()
        obj = {
            "book name": title,
            "date": date
        }
        self.books.append(obj)
        return (f"{title} added to books list")
    
