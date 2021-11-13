import math

def tarea(b,h):
    a = 0.5 * b * h
    return a

def tperi(s1,s2,b):
    p = s1 + s2 + b 
    return p
    
def carea(r):
    a = math.pi * r ** 2 
    return a 
   
def cperi(r):
    p = 2 * math.pi * r
    return p

def rparea(n,s):
    a = (s*s*n)/(4*math.tan(180/n))
    return a 

def rpperi(n,s):
    p = n * s 
    return p 

def sqarea(S):
    a = S * S 
    return a 
    
def sqperi(S):
    p = 4*S
    return p 

def rcarea(l,w):
    a = l * w 
    return a 
    
def rcperi(l,w):
    p = 2*(l + w)
    return p
    

while(1):
    print("MENU")
    print("1. Area and Perimeter of Triangle")
    print("2. Area and Perimeter of Circle")
    print("3. Area and Perimeter of Regular polygon")
    print("4. Area and Perimeter of Square")
    print("5. Area and Perimeter of Rectangle")
    print("6. Exit")
    ch = int(input("Enter your choice:"))
    if ch == 1:
        b = float(input("Enter base of triangle:"))
        h = float(input("Enter height of triangle:"))
        s1 = float(input("Enter side1 of triangle:"))
        s2 = float(input("Enter side2 of triangle:"))
        print("The area of triangle :",tarea(b,h))
        print("The perimeter of triangle :",tperi(s1,s2,b))
        
    elif ch == 2:
        r = float(input("Enter radius of circle:"))
        print("The area of circle :",carea(r))
        print("The perimeter of circle :",cperi(r))
    
    elif ch == 3:
        n = int(input("Enter the no of sides:"))
        s = float(input("Enter dimension of side:"))
        print("The area of regular polygon :",rparea(n,s))
        print("The perimeter of regular polygon :",rpperi(n,s))
    
    elif ch == 4:
        S = float(input("Enter side length:"))
        print("The area of square :",sqarea(S))
        print("The perimeter of square :",sqperi(S))

    elif ch == 5:
        l = float(input("Enter length of rectangle :"))
        w = float(input("Enter width of rectangle :"))
        print("The area of rectangle :",rcarea(l,w))
        print("The perimeter of rectangle :",rcperi(l,w))

    elif ch == 6:
        break
    else:
        print("INVALID INPUT")


    

