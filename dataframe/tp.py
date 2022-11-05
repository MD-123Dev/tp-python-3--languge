import pandas as pd
import csv

header = ['title',"author"]
data = [['book1','author1'],['book2','author2'],['book3','author3'],['book4','author2']]
dtFrame = pd.DataFrame(data,columns=header)

#get data in specif row
#print(dtFrame.loc[1])
#get row 0 and 2 
#print(dtFrame.loc[[0, 2]])


def getOne(rowIndex,colName):
    print(dtFrame._get_value(rowIndex, colName))

def getAll():
    print(dtFrame)


def removeOne(rowIndex):
    x = dtFrame.drop(rowIndex)
    print(x)

def removeCol(colName):
    data = dtFrame.drop(colName, axis=1)
    print(data)

def removeAll():
    data = dtFrame.drop(columns=['title', "author"])
    print(data)


def add(newRow):
    data = dtFrame.append(newRow, ignore_index=True)
    print(data)
   


def getAllTitle():
    data = dtFrame[["title"]]
    print(data)

def sortByTitle():
    data = dtFrame.sort_values(by='title', ascending=False)
    print(data)

def get():
    #print the columns
    for index, row in dtFrame.iterrows():
        print(row['title'])

def getMethodTwo():
    #print the columns
    for ind in dtFrame.index:
        print(dtFrame['title'][ind], dtFrame['author'][ind])
    

def importCsv():
    mydata = pd.read_csv('file/book.csv')
    data =pd.concat([dtFrame,mydata],ignore_index=True) 
    print(data)

    


def exportCsv():
    dtFrame.to_csv('file/book.csv', mode='a', index=False, header=False)
    fl = pd.read_csv('file/book.csv')
    print(fl)


#data display have same author value
def filterByAuthor(valueAuthor):
    
    data = dtFrame[dtFrame['author'] == valueAuthor]
    print(data)

     

########################################################

#getOne(2,'title')
#add({'title':'book5', 'author':'author6'})
#getAll()
#removeOne(2)
#removeCol("author")
#removeAll()
#getAllTitle()
#sortByTitle()
#get()
#getMethodTwo()
#importCsv()
#exportCsv()
#filterByAuthor('author2')

