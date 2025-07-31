n = int(input())
p = int(input())

# Calculate HCF
hcf = 0
t = min(n, p)  # Check only up to the smaller number

for i in range(1, t + 1):
    if n % i == 0 and p % i == 0:  # Check for common divisors
        hcf = i  # Update HCF to the largest common divisor

# Calculate LCM using the relationship: LCM = (n * p) / HCF
lcm = (n * p) // hcf

# Store results in a list
l1 = [lcm,hcf]
print(l1)


    