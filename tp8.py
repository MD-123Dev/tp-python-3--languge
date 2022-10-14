# Set

book = {"book1","book2","book3"}
numbers = {2,6,4,8,9,6,0}

def add(value):
    book.add(value)
    print(book)


def remove(value):
    book.remove(value)
    print(book)


def removeAll():
    book.clear()
    print(book)


def getAll():
    #1
    for x in book:
        print(x)


def getAllNumbers():
     for nb in numbers:
        print(nb)


#add("book5")
#remove("book2")
#removeAll()
#getAll()
getAllNumbers()