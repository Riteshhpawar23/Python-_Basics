#sorting

l1=[23,3,34,53,98,34,108]

# before sorting 
print(l1)
print("\n") 
print("after sorting ")
#after sorting

l1.sort()
print(l1)
 
print("\n")

#revers

l1.reverse()
print("after revers")
print(l1)
print("\n")

# append add value at the last index on list

l1.append(10)
print(" after appending 10")
print(l1)
print("\n")

# insert(2,8) this add 8 at index 2

l1.insert(2,8)
print(" after insert")
print(l1)
print("\n")

# pop(2) will remove vale at inder 2
l1.pop(2)
print(" after pop")
print(l1)
print("\n")

#remove(3) will remove 34 from list
l1.remove(3)
print("after remove")
print(l1)
print("\n")

# count number of element in list
n=l1.count(34)
print("count of 34")
print(n)
print("\n")

#index of element in list
n=l1.index(34)
print("give index of first 34")
print(n)


