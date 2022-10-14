#error handling 


try:
    f = open('file/file.csv')
    #f = open('file.csv')
    print(f.read())
except:

    print("no esixt  !!!!!! ")

