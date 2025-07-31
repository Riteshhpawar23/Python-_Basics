class Student :
    collegename=' terna college '  # gobal attribut
    def __init__(self,namee,markss): 
        self.fullname=namee   
        self.totalmarks=markss  
        
        print(" this is initilization function")
        
S1=Student('Ritesh',56)
print(S1.fullname,S1.totalmarks,S1.collegename) # gobal attribute can also be called using object 

S2=Student('Prachi',44)
print(S2.fullname,S2.totalmarks,Student.collegename) # gobal attribute can also be called using class name