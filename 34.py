import math

sum = 0
for num in xrange(3, 1000000):
    tempSum = 0
    for digit in str(num):
        tempSum += math.factorial(int(digit))
    if tempSum == num:
        sum += tempSum

print sum
