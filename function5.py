# gobal and local variable

a=3

def my(a):
    a=4          # a is local variable
    print(a)

my(a)

print(a)     # a is gobal variabl

print("\n")


#--------------------------------------------------------------------------------


x=5

def yo():
    global x                       # this function change local variable into gobal variable and gobal variable value wll change
    x=10
    print(x)

print(x)
yo()
print(x)