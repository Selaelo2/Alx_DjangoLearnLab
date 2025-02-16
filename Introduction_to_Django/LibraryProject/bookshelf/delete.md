# Delete Operation

**Command:**

```python
# Delete the book
book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")
book_to_delete.delete()

# Confirm the deletion by trying to retrieve the book again
Book.objects.all()
```
