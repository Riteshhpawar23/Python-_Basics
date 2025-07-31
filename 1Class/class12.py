#multile level heritances

class A:
    varA="welcome A..."

class B:
    varB="welcome B..."

class C(A,B):
    varC="welcome C..."

c1=C()

print(c1.varC)
print(c1.varB)
print(c1.varA)