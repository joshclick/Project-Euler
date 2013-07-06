def fib():
    x,y = 0,1
    while True:
        yield x
        x,y = y, x+y

def even(seq):
    for num in seq:
        if not num % 2:
            yield num

def underlim(seq):
    for num in seq:
        if num > 4000000:
            break
        yield num

print sum(even(underlim(fib())))