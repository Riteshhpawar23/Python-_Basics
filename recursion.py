n=int(input())

def ntime(n):
    print("hello world")
    print(n)
   
    if(n==0):
        return
    ntime(n-1)

ntime(n)