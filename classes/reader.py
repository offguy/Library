import datetime

class Reader:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.books = []

    def read_book(self, title):
        date = datetime.datetime.now().date().strftime("%d-%m-%Y, %H:%M")
        obj = {
            "title": title,
            "date": date
        }
        self.books.append(obj)
        return (f"{title} added to {self.name} books list")
    
