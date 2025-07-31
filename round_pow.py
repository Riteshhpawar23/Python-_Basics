# round fuction take round of function of floating data types
a=int(input("enter the radius--"))


pi=3.14159265359

b=pow(a,2)*pi  #pow function help to take power it syntax is (number at base, number at exponent, # it is Optional.number for modulus)

print("number befor round of-",b)
print()

# after round function

ans=round(b,0)            # round(number, digits)
                          #-number	Required. The number to be rounded ,
                          #-digits	Optional. The number of decimals to use when rounding the number. Default is 0

print("number after round of-",ans)