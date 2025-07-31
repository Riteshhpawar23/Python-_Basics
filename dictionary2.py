# accesing element in dictonary

fruit={"mango":120,"apple":140,'orange':100}

print(fruit["apple"])
print(fruit['orange'])
 #print(fruit['pineapple'])---> it cause the error has pineapple is not present 
 
# to overcome the error we use get
print('\n')
print(fruit.get('mango'))
print(fruit.get("pineapple"))
print(fruit.get("CHIKU",'NOT THERE')) #if there is not present then itshow next text or element avaible there

