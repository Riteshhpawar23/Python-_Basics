#Example=1

class Student :

    def __init__(self,namee,markss): # here self is connected to self=S1 and Ritesh=namee and 56=markss
        self.fullname=namee  # to access the name and mark we have to connect function parameter 
        self.totalmarks=markss  # to self with---> .(anyname) 
         # for object we are addinng [.anyname] so that object can identify it
        
        print(" this is initilization function")
        
S1=Student('Ritesh',56)
print(S1.fullname,S1.totalmarks)

S2=Student('Prachi',44)
print(S2.fullname,S2.totalmarks)

#Example=2

class Car:
    
    def __init__(self,carname,price):
        self.car=carname
        self.onroadprice=price
    

car1=Car("alto",12000)
print(car1.car,car1.onroadprice)