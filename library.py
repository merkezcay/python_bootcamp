# creating library class
class Library() :
    def __init__(self, file_name) :
        self.file_obj = open(file_name, "a+")
    # list a book from library
    def list_book(self):
        self.file_obj.seek(0)
        lines = self.file_obj.read().splitlines()
        for line in lines:
            book = line.split(",")
            print(f"\nBook: {book[0]}, Author: {book[1]}")
            
    # adding a book to library
    def add_book(self):
        title = input("Enter the book title: ")
        author = input("Enter the author: ")
        release = input("Enter the release year: ")
        page = input("Enter the number of pages: ")
        genre = input("Enter the book genre: ")

        book = title + "," + author + "," + release + "," + page + "," + genre
        self.file_obj.seek(0)
        self.file_obj.write(book + "\n")
        
    # removing a book from library
    def remove_book(self):
        title = input("Enter the book title: ")
        self.file_obj.seek(0)
        books = self.file_obj.read().splitlines()
        for book in books:
            removed = book.split(",")
            if title == removed[0] :
                # removing from the list
                books.remove(book)
                
                self.file_obj.truncate(0)

                for new_book in books : 
                    self.file_obj.write(new_book + "\n")
    # listing a book by genre
    def search_genre(self) :
        genre = input("Enter the book genre: ")
        self.file_obj.seek(0)
        books = self.file_obj.read().splitlines()
        for book in books :
            books_genres = book.split(",")
            if genre == books_genres[4]:
                print(f"{books_genres} \n")

    def __del__(self):
        self.file_obj.close()

# creating an object from the library class
lib = Library("books.txt")
# user input guide 
while True:
    user = input("""
* MENU *
1) List Books
2) Add Book
3) Remove Book
4) Search Genre
q) Quit
Enter your choice (1-4 or exit with q ): """)
        
    if user == "1" :
        lib.list_book()

    elif user == "2" :
        lib.add_book()
        
    elif user == "3" :
        lib.remove_book()

    elif user == "4":
        lib.search_genre()
    
    elif user == "q" :
        break

    else:
        break