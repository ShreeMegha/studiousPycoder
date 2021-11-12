''' BINARY TYPE FILE OPERATIONS '''

import pickle

def write():
    file = open("Doc.dat",'ab')
    record = []
    while True:
        rno = int(input("Enter the Roll no:"))
        name = input("Enter the Name:")
        data = [rno,name]
        record.append(data)
        ch = input("Do you want to enter records(y/Y/n/N):")
        if ch == "n" or ch == "N":
            break
    pickle.dump(record,file)

def read():
    file = open("Doc.dat",'rb+')
    while True:
        try:
            sfile = pickle.load(file)
            for i in sfile:
                print (i)
        except EOFError:
            break

def search():
    file = open("Doc.dat",'rb+')
    rno = int(input("Search for Roll no:"))
    found = 0
    try:
        while True:
            sfile = pickle.load(file)
            for i in sfile:
                if i[0]== rno:
                    print("RECORD FOUND")
                    print(i[0],i[1])
                    found = 1
                    break
    except Exception:
        file.close()
    if found == 0:
        print("RECORD NOT FOUND")
    else:
        print("RECORD FOUND")
        
while(1):
    print("OPERATIONS LIST")
    print("1. WRITE THE RECORD")
    print("2. READ THE RECORD")
    print("3. SEARCH THE RECORD")
    option = int(input("ENTER YOUR CHOICE:"))
    if option == 1:
        write()
    elif option == 2:
        read()
    elif option == 3:
        search()
    else:
        break
    ch = input("Do you want to continue operations(y/Y/n/N):")
    if ch == "y" or ch == "Y":
        continue
    else:
        break
    
    
        
