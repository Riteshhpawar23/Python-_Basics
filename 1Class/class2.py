class empolye:
    language="pyhton"  #This is a class attribute
    salary=12000

empolye1=empolye()
empolye1.name='ritesh'    # this is instances attribute

print(empolye1.name,empolye1.salary,empolye1.language)


empolye2=empolye() 
empolye2.name="prachi"   
empolye2.language='html'  # here instances attribute overwrite the class attribute

print(empolye2.name,empolye2.salary,empolye2.language)