# function  

def total() :
    numbers = [1,12,51,62,4]

    tot = 0

    for x in numbers:
        tot = tot + x 
    return tot



print(total())

# 2

def book():
    print("book")


book()

# 3 

def sum(x,y,f):
    z = int(x) + int(y) + int(f)
    print(z)

sum(2,5,7)

#4

rst = lambda  a,b,z : a + b + 1 + z

print("lambda",rst(4,5,6))

#5 recursive function 

def clc(n):
    if n==1:
        return 1
    else:
        return n + clc(n-1)


print(clc(10))

