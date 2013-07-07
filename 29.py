powList = []
for a in xrange(2, 101):
    for b in xrange(2, 101):
        powList.append(a**b)

print len(set(powList))
