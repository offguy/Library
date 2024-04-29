from .shelf import Shelf
from .reader import Reader

class Library:
    def __init__(self, num_of_shelves=3):
        self.shelves = []
        self.readers = []
        self.id_count = 1
        for i in range(1, num_of_shelves + 1): 
            shelf_name = f"Shelf {i}"  
            shelf = Shelf(name=shelf_name)  
            self.shelves.append(shelf)
            
    def print_all_shelves(self):
        for s in self.shelves:
            print(s.books_on_shelf)

    def is_there_place_for_new_book(self):
        for shelf in self.shelves:
            if shelf.is_shelf_full == False:
                return "There is room for more books!"
        return "There is no more place in the library"

    def add_new_book(self, author, title, num_of_pages):
        for s in self.shelves:
            if not s.is_shelf_full:
                s.add_book(author, title, num_of_pages)
                return f"{title} by {author} added to the library!"
        return "No more place for books"

    def delete_book(self, book_name):
        for s in self.shelves:
            for b in s.books_on_shelf:
               if b.title == book_name:
                   s.books_on_shelf.remove(b)
                   return(f"{b.title} was deleted")
        return "book not found"
    
    def change_locations(self, book_title1, book_title2):
        # Find the shelves containing the books with the specified titles
        shelf1 = next((s for s in self.shelves if any(b.title == book_title1 for b in s.books_on_shelf)), None)
        shelf2 = next((s for s in self.shelves if any(b.title == book_title2 for b in s.books_on_shelf)), None)

        # Check if both books are found in different shelves
        if shelf1 is not None and shelf2 is not None and shelf1 != shelf2:
            # Find the books within their respective shelves
            book1 = next(b for b in shelf1.books_on_shelf if b.title == book_title1)
            book2 = next(b for b in shelf2.books_on_shelf if b.title == book_title2)

            # Get the indices of the books within their shelves
            index1 = shelf1.books_on_shelf.index(book1)
            index2 = shelf2.books_on_shelf.index(book2)

            # Swap the books between shelves
            shelf1.books_on_shelf[index1], shelf2.books_on_shelf[index2] = shelf2.books_on_shelf[index2], shelf1.books_on_shelf[index1]
            return "Books' locations changed successfully."

        return "One or both books not found in different shelves."
    
    def chang_place_in_shelf(self, shelf_num, book1_location, book2_location):
        shelf_name = f"Shelf {shelf_num}"
        if shelf_name not in next(s.name for s in self.shelves):
            return f"Shelf {shelf_num} doesn't exist"
        shelf = next(s for s in self.shelves if s.name == shelf_name)
        if book1_location -1 >= len(shelf.books_on_shelf) or book2_location -1 >= len(shelf.books_on_shelf):
            return "Invalid book location"        
        return shelf.replace_books(book1_location -1, book2_location -1)
    
    def order_all_books(self):
        for s in self.shelves:
            s.orgenize_books_by_pages()
        return "books in order"

    def register_reader(self, name):
        is_exist = next((r.name for r in self.readers if r.name == name), None)
        if not is_exist:
            new_reader = Reader(self.id_count, name)
            self.id_count +=1
            self.readers.append(new_reader)
            return f"Reader {name} (id: {self.id_count}) created"
        return f"Reader id {name} is in use"

    def remove_reader(self, name):
        is_exist = next((r for r in self.readers if r.name == name), None)
        if not is_exist:
            return "reader not found"
        self.readers = [x for x in self.readers if x.name != name]
        return f"reader {name} removed"
    
    def reader_read_book(self, reader_id, book_name):
        reader = next((r for r in self.readers if r.id == reader_id), None)
        is_book = next((s for s in self.shelves if any(b.title == book_name for b in s.books_on_shelf)), None)
        if not reader:
            return f"reader {reader_id} not exist"
        elif not is_book:
            return f"{book_name} isn't in the library"
        return (reader.read_book(book_name) + f" of reader {reader_id}")
        
    def search_by_author(self, author):
        author_books = [b.title for s in self.shelves for b in s.books_on_shelf if b.author == author]
        if author_books:
            return f"{author}'s books: {author_books}"
        return f"No books by {author}"
