name=str(input("enter the name-"))
f={}
for i in name:
    if i not in f:
        f[i]=1
    else:
        f=f+1

print(f)           