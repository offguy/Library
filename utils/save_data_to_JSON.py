import json

def serialize_book(book):
    return {
        "author": book.author,
        "name": book.title,
        "num_of_pages": book.num_of_pages
    }

def serialize_reader(reader):
    return {
        "id": reader.id,
        "name": reader.name,
        "books": [
            {"title": book["title"], "date": book["date"]}
            for book in reader.books
        ]
    }

def save_library_data_to_file(library):
    data = {
        "id_count": library.id_count,
        "shelves": [
            {
                "name": shelf.name,
                "books_on_shelf": [serialize_book(book) for book in shelf.books_on_shelf],
                "is_shelf_full": shelf.is_shelf_full
            }
            for shelf in library.shelves
        ],
        "readers": [serialize_reader(reader) for reader in library.readers]
    }
    path = "Lessons\\Projects\\Library\\utils\\Library.json"
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    return "data saved"