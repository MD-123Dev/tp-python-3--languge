from Book import Book

class Author(Book):

    def __init__(self, name):
        self.name = name
       
         

    def getName(self):
        return self.name
