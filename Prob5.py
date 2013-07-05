thenum = 0
number = 20
while not thenum:
    thenum = number
    for factor in xrange(1, 21):
        if number % factor:
            thenum = 0
            break
    number += 20

print thenum
