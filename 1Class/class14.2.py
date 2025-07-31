class Person:
    name="anonymous"
    
    def changename(self,name):
        self.__class__.name=name # another method to change class name or object namer
        
 
p1=Person()   
p1.changename("ritesh pawar")
print(p1.name)

#-----------------------------------------------------------------------------------------------------------#

class Person:
    name="anonymous"
    
    def changename(self,name):
        self.__class__ # another method to change object name
        
 
p1=Person()   
p1.changename("ritesh pawar")
print(p1.name)