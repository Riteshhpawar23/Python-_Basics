# check if element is present in dictionary or not

fruit={"mango":120,"apple":140,'orange':100,"chiku":80,"banana":40,"starfruit":20}
print("apple" in fruit)
print("pineapple" in fruit)
print("\n")

# removing element form is dictionary 

fruit.pop("apple")\
 
print(fruit)

# pop.item will remove last element form dictionary

fruit.popitem()

print(fruit)           #if all items are removed from dictionary then it show empty dictionary

# delete whole dictionary 

del fruit

# it will show error as there is no dictuonary is present
print(fruit)