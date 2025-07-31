# method for class

class Student :

     def __init__(self,namee,markss):
        self.fullname=namee  
        self.totalmarks=markss 
        
     def hello(self):             # methods are the function like hello which print msg and  
         print("hello students",self.fullname) # It is necssary to pass  in function or it will show the error
     
     def allstudentmarks(self):
         return(self.totalmarks)
        
S1=Student('Ritesh',56)   
S1.hello()                     # this how you call function [ directly]

print(S1.allstudentmarks())   # this how you call funtion using return


