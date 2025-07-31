# if you don't want to some part of  code to execute in code then use pass

for i in range(1,9):
    pass
 
 
 # if you  don't part certain part of code to exeute in code then we use continue    
 
for i in range (0,8):
    if i==4:
        continue  # it skip the 5 in for loop
    print(i)
 # it will stop the code at the given condition  
 
 
print("\n")
for i in range (0,11):
    if i==5:
        break  # it break loop at the 5
    print(i)