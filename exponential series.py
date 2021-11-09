x=float(input("enter value of x:"))
y=int(input("enter limit:"))
s=0
for i in range(y+1):
    fact=1
    for k in  range (1,i+1):
        fact =fact*k
    s+=(x**i)/fact
print(s)
