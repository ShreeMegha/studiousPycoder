i=int(input("enter the limit:"))
x=0
y=1
z=1
print("Fibonacci series\n")
print(x,y,end=" ")
while(z<=i):
    print(z,end=" ")
    x=y
    y=z
    z=x+y
    
