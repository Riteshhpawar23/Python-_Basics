class Account:
    
    def __init__(self,accno,accpin):
        self.accountNo=accno
        self.__accountpin=accpin
        
        
        
    def restpassord(self):       # you cannot called priavte directly but you can call it from  within 
        print(self.__accountpin) # method means call it indirectly using other method( function)
  
  
  
  
a1=Account("RP23092003",2326)    # some sensitive informtion need to keep private that is done by private functiom
                                 # synatx of that is[ __(attribute or object)] that you want to make private
                                 #it show no attribute ex-__accountpin is not present bit if you remove __ it showwe that


print(a1.accountNo)#,#a1.accountpin)   # uncomment this line to for better explaination
              
print(a1.restpassord())
        