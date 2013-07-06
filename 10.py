import math

plist = [2]

def get_primes(max):
    yield 2
    for num in xrange(3, max, 2):
        for p in plist:
            if num % p == 0: break
        if num % p:
            plist.append(num)
            yield num

print sum(get_primes(2000000))

# super inefficient