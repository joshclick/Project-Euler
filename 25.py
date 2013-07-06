def fib():
    i,x,y = 0, 0, 1
    while True:
        yield str(i) + " " + str(x)
        i,x,y = i+1, y, x+y


def underlim(seq):
    for num in seq:
        if len(num.split()[1]) == 1000:
            return num.split()[0]

print underlim(fib())

# inefficient