class Person:
    name="anonymous"
    
    @classmethod
    def changename(Person,name): #we can change the class name by @classmethod and 
        Person.name=name         #In bracket(),can be anyname example-Person can be change into anything
        
 
p1=Person()   
p1.changename("ritesh pawar")
print(Person.name)  #class name is change into ritesh pawar from anonymous 