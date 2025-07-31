class classroom:
    
    def __init__(self,name,rollno):
        self.fullname=name
        self.id=rollno

s1=classroom('Ritesh',45)
print(s1.fullname,s1.id)

del s1.fullname  #del will delete the object attribute ,method or object itself

print(s1.fullname,s1.id) #it will give error as s1.fullname is deleted