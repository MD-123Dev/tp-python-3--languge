#1 list 

lst = ["book1","book2","book3"]
lst2 = [5,6,4,1,3,8]
lst3 = ["phone1","phone2"]

def add(x):
    lst.append(x)
    print(lst)

def remove(x):
    index = lst.index(x)
    lst.pop(index)
    print(lst)


def removeAll():
    lst.clear()
    print(lst)


def upadte(x ,value):
    index = lst.index(x)
    lst[index] =  value
    print(lst)


def sort():
    lst2.sort()
    print(lst2)


def joinList():
    lst.extend(lst3)
    print(lst)


def getAll():
    for x in lst:
        print(x)


def countLst(ls):
    x = len(ls)
    print(x)


#getAll()
#joinList()
#add("book5")
#remove("book2")
#removeAll()
#upadte("book2","book10")
#sort()
#joinList()
#countLst(lst2)