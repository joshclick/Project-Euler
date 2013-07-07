nsum = 0

def is_double_pal(num):
    if not str(num) == str(num)[::-1]:
        return 0
    binStr = "{0:b}".format(num)
    if not binStr == binStr[::-1]:
        return 0
    return num

for i in xrange(1000000):
    if is_double_pal(i):
        nsum += i

print nsum
