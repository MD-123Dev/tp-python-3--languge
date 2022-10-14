#dictionary

book = {
    "title":"jjd",
    "category":"catg1",
    "price":45
    
}

def getOne(key):
    print(book.get(key))


def add(key,value):
    book[key] = value
    print(book)


def remove(key):
    
    book.pop(key)
    print(book)


def removeAll():
    book.clear()
    print(book)


def upadte(x, value):
    book.update({x: value})
    print(book)



def getAllValue():
    print(book.values())


def getAll():
    #1
    for x in book:
        print("value",book[x])
  

def getAllMethodeTwo():
    #2
    for key, value in book.items():
         print(key, value)
            


getOne("title")
#getAll()
#getAllMethodeTwo()
#getAllValue()
#upadte("category","categ2")
#removeAll()
#remove("title")
#add("ator","atoc")
