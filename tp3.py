#loop 

x=1
while x <= 10:
    print(x,"hello",sep="=>")
    x += 1


#2

books = ["book1","book2","book3"]

for x in books:
    print(x)
    if x=="book2":
        print(books[0])
        break

#3

numbers = [1,12,51,62,4]

tot = 0

for x in numbers:
    tot = tot + x 
print("total",tot)
    
#

for i in range(5,10):
    print(i)

#jump with  2 
for i in range(1,10,2):
    print(i)

#

books = ["book1","book2","book3","book4"]

for i in range(0,4,2):
    print(books[i])

#
arr1 = [1,5,7,8]
arr2 = [5,6,9]
arr3 = []
for x in range(0,4):
    for y in range(0,3):
        clc = arr1[x] * arr2[y]
        arr3.append(clc)
    
print(arr3)
