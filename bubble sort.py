def main():
    l=[42,29,74,11,65]
    n=len(l)
    print("original list: ",l)
    for i in range(n-1):
        for j in range (n-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    print("list after sorting is: ",l)
    
