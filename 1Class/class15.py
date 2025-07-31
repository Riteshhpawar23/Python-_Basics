class Student:
    def __init__(self,phy,math,eng):
        self.phy=phy
        self.math=math
        self.eng=eng
    
    @property   #property method is use change attribute of object 
    def percentage(self):
        return str(self.phy+self.math+self.eng//3)+"%"
    
std1= Student(90,93,95)
print(std1.percentage)

std1.phy=86

print(std1.percentage)