dup=n
count=0
sum=0
while n>0:
    count+=1
    digit=n%10
    n=n//10
print(count)
while dup>0:
    digit=dup%10
    print(digit)
    sum=sum+(pow(digit,count))
    dup=dup//10
print(sum)
if sum==dup:
    print(True)
else:
    print(False)