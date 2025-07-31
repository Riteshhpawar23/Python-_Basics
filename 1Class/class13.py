
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
    def __init__(self,type,model):
        self.type=type
        super().__init__(model)      # SUPER is use to acess the method of parent class 
        super().start                # mean that we can call inner class from first class
                                     # example--here model is called from toyota call using super and model class is different



car1=toyota("petrol","a134")

print(car1.model)
print(car1.start())