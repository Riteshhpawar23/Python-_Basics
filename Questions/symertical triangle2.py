n=int(input())

for i in range(0,1+n):
    for j in range (i):
        print("*",end=" ")
    
    space=n-i
    print(" "*4*space, end="")
    for j in range (i):
        print("*",end=" ")
    print( )

for t in range(n-1):
    
    for k in range(n-t-1):
        print("*",end=" ")
        
    space1= t+1
    print(" "*space1*4,end="")
    for k in range(n-t-1):
        print("*",end=" ")
    print()
    
   