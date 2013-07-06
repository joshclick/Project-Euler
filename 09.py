for a in xrange(1, 1000):
    for b in xrange(a+1, 1000):
        c = 1000 - b - a
        if c*c == a*a + b*b:
            print a*b*c
            break
