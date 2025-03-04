from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author (e.g., author with name 'J.K. Rowling')
def get_books_by_author():
    author_name = 'J.K. Rowling'
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)  # Using filter to get books by the specific author
    for book in books:
        print(f'Book: {book.title} by {author.name}')

# 2. List all books in a library (e.g., library with name 'Central Library')
def get_books_in_library():
    library_name = 'Central Library'
    library = Library.objects.get(name=library_name)
    books = library.books.all()  # This works since it's a ManyToMany relationship
    for book in books:
        print(f'Book: {book.title} in {library.name}')

# 3. Retrieve the librarian for a specific library (e.g., library with name 'Central Library')
def get_librarian_for_library():
    library_name = 'Central Library'
    library = Library.objects.get(name=library_name)
    librarian = library.librarian  # Since it's a OneToOneField relationship
    print(f'Librarian for {library.name}: {librarian.name}')


if __name__ == "__main__":
    get_books_by_author()
    get_books_in_library()
    get_librarian_for_library()
