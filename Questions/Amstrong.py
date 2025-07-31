n=int(input())


def checkArmstrong(n):
    original = n  # Store the original number
    count = len(str(n))  # Calculate number of digits directly
    total_sum = 0

    while n > 0:
        digit = n % 10
        total_sum += pow(digit, count)
        n //= 10

    if total_sum == original:
        return(True)
    else:
        return(False)

k=checkArmstrong(n)

print(k)