# this function is used when we need nameless function for short periods

a=2
b=5


def add (a,b):
    return print(a+b)

add(a,b)

# using lambda function

(lambda a,b:print(a+b)) (a,b) #(a,b) are the parameter id it is not present then it dont show output


