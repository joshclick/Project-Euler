import math

plist = [2]

def primes(min, max):
    if 2 >= min: yield 2
    for i in range(3, int(math.sqrt(max) + 1), 2):
        for p in plist:
            if i % p == 0: break
        if i % p:
            plist.append(i)
            if i >= min: yield i

def factors(number):
    for prime in primes(2, number):
        if number % prime == 0:
            number /= prime
            yield prime
        if number == 1:
            break

print max(factors(600851475143))
