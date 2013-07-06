import math

nstr = str(math.factorial(100))

nsum = sum(int(digit) for digit in nstr)
print nsum
