name=str(input("enter the name--"))

age=int(input("enter the age--"))

hobby=str(input("enter the hobby--"))

def intro(name,age,hobby):
    
    return(name,age,hobby)

c=intro(name,age,hobby)   #multiple value can be stored into one variable it type is tuple

print(c,type(c))
print("\n")

#------------------------------------------------------------------------
c,d,e=intro(name,age,hobby)             # different variable can be use to store different value and will give recpective as output
print(c,type(c))
print(d,type(d))
print(e,type(e))
