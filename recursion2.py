def oneton(k, n):
    if k > n:  # Base case: stop when k exceeds n
        return
    print(k)
    oneton(k + 1, n)  # Recursive call with incremented k

n = int(input("Enter a number: "))
oneton(1, n)  # Start from 1
