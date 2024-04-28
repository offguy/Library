def load_initial_data(l, db):
    books_collection = db["books"]
    books = list(books_collection.find({}))
    books_added = 0
    for s in l.shelves:
        for i in range(2):
            if books_added < len(books):
                s.add_book(books[books_added]["author"],books[books_added]["title"],books[books_added]["num_of_pages"])
                books_added += 1
            else:
                break
