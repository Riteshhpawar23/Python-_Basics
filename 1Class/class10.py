# Inheritances Of Class

class Car:
    color="Black"
    @staticmethod   
    def start():
        print("car is started...")   
    @staticmethod
    def stop():
        print("car is stopped...")       
class toyota(Car):   
    def __init__(self,name):
        self.carname=name      
         
car1=toyota("fortuner")   
car2=toyota("hilex")

print(car1.color)
print(car2.carname)
car1.start()
car2.stop()