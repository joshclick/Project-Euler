plist = [2]

for num in xrange(3, 100000, 2):
    for p in plist:
        if num % p == 0:
            break
    if num % p:
        plist.append(num)

circPrimeCount = 0

for nPrime in plist:
    for mPrime in plist:

# incomplete