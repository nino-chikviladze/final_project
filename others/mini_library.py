def main():
    library = [
        {"title": "War and Peace", "author": "Leo Tolstoy", "year": 1869},
        {"title": "Moby-Dick", "author": "Herman Melville", "year": 1851},
        {"title": "1984", "author": "George Orwell", "year": 1949},
        {"title": "The Brothers Karamazov", "author": "Fyodor Dostoevsky", "year": 1880},
        {"title": "The Catcher in the Rye", "author": "J. D. Salinger", "year": 1951},
        {"title": "Gone With the Wind", "author": "Margaret Mitchell", "year": 1936},
        {"title": "Dark Matter", "author": "Blake Crouch", "year": 2016},
        {"title": "Jane Eyre", "author": "Charlotte Brontë", "year": 1847},
        {"title": "Crime and Punishment", "author": "Fyodor Dostoevsky", "year": 1866},
        {"title": "On the Road", "author": "Jack Kerouac", "year": 1957},
    ]

    while True:
        show_menu()
        choice = input("Select an option (1-5): ")
        print()

        match choice:
            case "1":
                show_all_books(library)

            case "2":
                t = input("Enter title: ")
                a = input("Enter author: ")
                y = input("Enter publication year: ")
                add_new_book(library, t, a, y)
                print(f'"{t}" has been added to the library!')

            case "3":
                t = input("Enter the title of the book to search for: ")
                b = search_book(library, t)
                if b:
                    print(f'Found: "{b['title']}" by {b['author']} ({b['year']})')
                else:
                    print("This book was not found in the library.")

            case "4":
                t = input("Enter the title of the book you want to borrow: ")
                if checkout_book(library, t):
                    print(f'The book "{t}" has been checked out for reading!')
                else:
                    print("This book is not available in the library.")

            case "5":
                print("Exiting the program.")
                break

            case _:
                print("Invalid choice. Please select an option between 1 and 5.")
        print()


def show_menu():
    print("<----- Mini-Library Menu ----->")
    print("1. View all books")
    print("2. Add a new book")
    print("3. Search for a book by title")
    print("4. Borrow a book")
    print("5. Exit program")

def show_all_books(library):
    print("<------------- Books in the Library ------------->")
    for index, book in enumerate(library, 1):
        print(f'{index}. "{book['title']}" by {book['author']}')

def add_new_book(library, title, author, year):
    library.append({"title": title, "author": author, "year": year})

def search_book(library, title):
    for book in library:
        if book["title"] == title:
            return book
    return None

def checkout_book(library, title):
    book = search_book(library, title)
    if book:
        library.remove(book)
        return True
    return False


if __name__ == "__main__":
    main()
