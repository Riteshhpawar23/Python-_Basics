class Person:
    name="anonymous"
    
    def changename(self,name):
        self.name=name
        
 
p1=Person()   
p1.changename("ritesh pawar")
print(p1.name) # it is objectname
print(Person.name)  # it is class name