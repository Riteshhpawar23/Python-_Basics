#multi level inhertiances

class Car:
    
    @staticmethod
    def start ():
        print("car is started...")
    @staticmethod
    def stoped():
        print("car is stoped...")

class model(Car):
    def __init__(self, model):
        self.model=model
        
class toyota(model):
    def __init__(self,type):
        self.type=type



car1=toyota("petrol")

print(car1.type)

#print(car1.model)       # here we cannot access the model from toyota classs
                          # because it donot get arrgument 
                          # do access it is done in class13.py
                           
         