# Delete Operation

**Command:**

```python
# First, import the Book model
from bookshelf.models import Book

# Retrieve the book to delete
book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book_to_delete.delete()

# Confirm the deletion by trying to retrieve all books again
Book.objects.all()
```
