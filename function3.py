a=int(input("enter the number one-"))
b=int(input("enter the number two-"))

def sum(a,b):
    print(a+b)

c=sum(a,b)    

print(c,type(c))        # if there is no return then funtion return none type
#-------------------------------------------------------------------------------------------------------------------------------#

a=int(input("enter the number 1-"))
b=int(input("enter the number 2-"))

def sum(a,b):
   c=a+b
   return c

c=sum(a,b)    

print(c,type(c))       # if there is  return then funtion return type output