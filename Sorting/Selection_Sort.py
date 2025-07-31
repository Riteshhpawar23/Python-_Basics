def selection_sort(arr,n):
    for i in range(n-1):
        minn=i 
        for j in range(i+1,n-1):
            if arr[j]<arr[minn]:
                minn=j
        arr[minn],arr[i]=arr[i],arr[minn]
    return arr

n=int(input("Enter The Size OF Arrya--"))
arr=[]
for i in range(n):
    k=int(input())
    arr.append(k)

s=selection_sort(arr,n)
print(s)