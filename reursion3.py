def dum(k,n,kum):
    
    kum=k*kum
    
    if k>=n:
        return kum
    return dum(k+1,n,kum)

n=int(input())

s=dum(1,n,kum=1)
print(s)
    