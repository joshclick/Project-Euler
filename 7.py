import math

idx = 1
theprime = 3
num = 3
while idx != 10001:
    prime = True
    for fact in xrange(2, int(math.sqrt(num) + 1)):
        if not num % fact:
            num += 2
            prime = False
            break
    if prime:
        idx += 1
        theprime = num
        num += 2

print theprime

# super messy