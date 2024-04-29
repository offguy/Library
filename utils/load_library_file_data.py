import json
from classes.book import Book
from classes.reader import Reader
from classes.shelf import Shelf


def deserialize_book(book_data):
    return Book(book_data["author"], book_data["name"], book_data["num_of_pages"])

def deserialize_reader(reader_data):
    reader = Reader(reader_data["id"], reader_data["name"])
    for book_data in reader_data["books"]:
        book = deserialize_book(book_data)
        reader.books.append(book)
    return reader

def load_library_data_from_file(library):
    path = "Lessons\\Projects\\Library\\utils\\Library.json"
    with open(path, "r") as f:
        data = json.load(f)
        # Load shelves
        shelves = []
        for shelf_data in data["shelves"]:
            shelf = Shelf(shelf_data["name"])
            # Load books on shelf
            for book_data in shelf_data["books_on_shelf"]:
                book = Book(book_data["author"], book_data["name"], book_data["num_of_pages"])
                shelf.books_on_shelf.append(book)
            shelf.is_shelf_full = shelf_data["is_shelf_full"]
            shelves.append(shelf)
        library.shelves = shelves
        readers = []
        for reader_data in data["readers"]:
            reader = Reader(reader_data["id"], reader_data["name"])
            # Load books read by reader
            for book_data in reader_data["books"]:
                book = {"title": book_data["title"], "date": book_data["date"]}
                reader.books.append(book)
            readers.append(reader)
        library.readers = readers
        library.id_count = data["id_count"]
    return "data loaded"