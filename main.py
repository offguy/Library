from classes.library import Library
from utils.db import db
from utils.load_initial_data import load_initial_data
from utils.save_data_to_JSON import save_library_data_to_file
from utils.load_library_file_data import load_library_data_from_file
l = Library()
load_initial_data(l,db)

def librar_simulator():
    is_exit = False
    while not is_exit:
        print("WELCOME... TO THE LIBRARY!")
        print("Please select what whould you like to do:")
        print("Adding a new book - Select 1")
        print("Deleting a book - Select 2")
        print("Changing books location - Select 3")
        print("Registrating a new reader - Select 4")
        print("Removing a reader - Select 5")
        print("Shearching a book bu author - Select 6")
        print("Reading a book by a reader - Select 7")
        print("Ordering all books - Select 8")
        print("Save all Liabrary data - Select 9")
        print("Load saved data - Select 10")
        print("Exit - Select 11")
        choice = int(input("enter choise number: "))

        if choice > 11:
            print("Invalid Choice!")
        elif choice == 1:
            is_place = l.is_there_place_for_new_book()
            if is_place == "There is room for more books!":
                print("adding a new book")
                author = input("Enter the books author: ")
                title = input("Enter the books title: ")
                num_of_pages = int(input("Enter the books number of pages: "))
                print(l.add_new_book(author, title, num_of_pages))
            else:
                print(is_place)
        elif choice == 2:
            print("DELETE a book")
            del_title = input("enter book title: ")
            print(l.delete_book(del_title))
        elif choice == 3:
            print("Changing books locations")
            location1 = input("enter book title: ")
            location2 = input("enter book title: ")
            print(l.change_locations(location1,location2))
        elif choice == 4:
            print("Registrating new reader")
            name = input("enter reader user name: ")
            print(l.register_reader(name))
        elif choice == 5:
            print("REMOVING a user")
            name = input("enter user name: ")
            print(l.remove_reader(name))
        elif choice == 6:
            print("Searching author")
            author = input("enter author name: ")
            print(l.search_by_author(author))
        elif choice == 7:
            print("Reader book reading")
            id = int(input("enter reader id: "))
            book_name = input("enter book title: ")
            reader = list(filter(lambda x: x.id == id ,l.readers))[0]
            print(reader.read_book(book_name))
        elif choice == 8:
            print(l.order_all_books())
        elif choice == 9:
            print(save_library_data_to_file(l))
        elif choice == 10:
            print(load_library_data_from_file(l))
        else:
            print("Good Bye")
            is_exit = True
librar_simulator()