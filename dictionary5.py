fruit={"mango":120,"apple":140,'orange':100,"chiku":80,"banana":40,"starfruit":20}

# it will print all keys
for i in fruit:
    print(i)
print("\n")

# it will print all valves
for i in fruit:
    print(fruit[i])
print("\n")   

# both key and value
for i in fruit:
    print(i,fruit[i])
print("\n")

#using dict.item()

for key,value in fruit.items():
    print(key,value)