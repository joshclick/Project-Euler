r = xrange(1, 101)
s = sum(r)
diff = s * s - sum(i*i for i in r)
print diff
