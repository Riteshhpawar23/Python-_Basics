# updating new dictionary

fruit={"mango":120,"apple":140,'orange':100}

fruit["pineapple"]=160

print(fruit)
print("\n")


# updating existing value

fruit["mango"]={"small mango":110,"large mango":120}

print(fruit)
print("\n")

# adding a new dictionary into existing dictionary

new={"chiku":80,"banana":40,"starfruit":20}
fruit.update(new)                             # two dictionary get join 
print(fruit)