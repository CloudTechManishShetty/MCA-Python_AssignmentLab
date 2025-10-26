# library/books.py

book_list = []

def add_book(title, author):
    book = {"title": title, "author": author, "status": "Available"}
    book_list.append(book)
    print("Book added: ",title," by ",author)

def remove_book(title):
    global book_list
    original_len = len(book_list)
    book_list = [b for b in book_list if b['title'].lower() != title.lower()]
    if len(book_list) < original_len:
        print("Book removed: ",title)
    else:
        print("Book not found: ",title)

def search_book(title):
    results = [b for b in book_list if title.lower() in b['title'].lower()]
    print("--- Search Results for ",title," ---")
    if results:
        for book in results:
            print("Title: ",book['title']," Author: ",book['author']," Status: ",book['status'])
    else:
        print("No books found matching the search criteria.")