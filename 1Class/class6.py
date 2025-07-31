
class student :
    
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    def avg(self):
        sum=0
        for val in self.marks :
            sum+=val
            
        print(" hi",self.name,"your avg marks are -",sum/3)

s1=student("ritesh",[10 ,20, 30])

s1.avg()