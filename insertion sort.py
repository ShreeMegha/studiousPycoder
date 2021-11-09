l=[70,49,31,6,65,81,68]
print("original list: ",l)
for i in l:
    j=l.index(i)
    while j>0:
        if l[j-1]>l[j]:
            l[j-1],l[j]=l[j],l[j-1]
        else:
            break
        j=j-1
print ("list after soortti:",l)
