maxSum = 0

for a in xrange(1, 100):
    for b in xrange(1, 100):
        nPow = a ** b
        digSum = sum(int(digit) for digit in str(nPow))
        if digSum > maxSum:
            maxSum = digSum

print maxSum
