# library.py

books_db = {}
issued_books = {}

def add_book(book_id, title, author, copies=1):
    if book_id in books_db:
        books_db[book_id]["copies"] += copies
        return f"Added {copies} more copies."
    books_db[book_id] = {"title": title, "author": author, "copies": copies}
    return f"Book '{title}' added."

def issue_book(student_id, book_id):
    if book_id not in books_db or books_db[book_id]["copies"] == 0:
        return "Book not available."
    issued_books.setdefault(student_id, []).append(book_id)
    books_db[book_id]["copies"] -= 1
    return f"Book {book_id} issued to {student_id}."

def return_book(student_id, book_id):
    if student_id not in issued_books or book_id not in issued_books[student_id]:
        return "No record found."
    issued_books[student_id].remove(book_id)
    books_db[book_id]["copies"] += 1
    return f"Book {book_id} returned by {student_id}."

def view_issued_books(student_id=None):
    if student_id:
        return issued_books.get(student_id, [])
    return issued_books
