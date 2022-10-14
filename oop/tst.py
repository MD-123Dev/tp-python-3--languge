import Book
import Author


bk = Book.Book("book1",41)
bk.addBook("book3")
print(bk.getBook())

#with Inheritance
at = Author.Author("author1")
at.addBook("book3")
print("book Info : ",at.getBook(),at.getName())