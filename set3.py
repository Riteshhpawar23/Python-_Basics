# intersection ---------------// for better understanding see diagram on google

python={"ritesh","kewal","sohil","ritesh","roshan",3,2}
java={"dashrath","harshal","kdk","modak0","ritesh",3,1,4}
c={134,434,43}



print(python.intersection(java))           # it give common element between two sets

#union---------------// for better understanding see diagram on google

print(python.union(java,c))                  # it will combine the set

#difference---------------// for better understanding see diagram on google

print(python.difference(java))     # it give element which are only in python if it present in both set then it will not show
                                     # ie- ritesh is in both set ie python,java then it will not show