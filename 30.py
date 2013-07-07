theSum = 0

for i in xrange(11, 200000):
    powSum = sum(int(digit) ** 5 for digit in str(i))
    if powSum == i:
        print powSum
        theSum += powSum

print theSum
