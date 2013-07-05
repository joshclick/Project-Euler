def multiples_of_3_or_5():
    for num in xrange(1000):
        if not num % 3 or not num % 5:
            yield num

print sum(multiples_of_3_or_5())
