#String 

StringOne = "hello"
StringTwo = "welcome"
StringTree = "hello"
txt = "hello - welcome "

def compareString(x,y):
    if x == y :
        print("is equal ")
    else:
        print("Not equal !!!!")


def replaceString(value, new):
    newValue = txt.replace(value, new)
    print(newValue)






def getChart(c):
    print(StringOne.find(c))



def SliceString():
   
    print(StringOne[2:])



def separateString():
    x = txt.split("-")
    for y in x:
        print(y)
    


compareString(StringOne,StringTwo)
#replaceString("welcome","come")
#getChart('o')
#SliceString()
#separateString()
