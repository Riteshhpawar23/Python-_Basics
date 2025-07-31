n = int(input("Enter the number of rows: "))

for i in range(0,n+1):
    for j in range(n,i,-1):
        print("*",end=" ")
        
    space=4*i
    if(i!=n):
        print(" "*space,end="")
    else:
        break
    
    
    for k in range(n,i,-1):
        print("*",end=" ")
    if(i!=n):
        print()
    else:
        break

     
for r in range(1,n+1):
    for t in range(0,r):
        print("*",end=" ")  
    space1=n-r
    print(" "*space1*4,end="")
    
    for l in range(0,r):
        print("*",end=" ")
    print( )