#tuple :> Once a tuple is created, you cannot change its values

tuple1 = ("book1", "book2", "book3")



def getAll():
    for x in tuple1:
        print(x)


def countTuple(ls):
    x = len(ls)
    print(x)

def getOne(x):
    index = tuple1.index(x)
    lst = list(tuple1)
    print(lst[index])


#getAll()
#countTuple(tuple1)
getOne("book2")
