maxpal = 0

def palindrome(num):
    s = str(num)
    if s == s[::-1]:
        return True

for i in xrange(1000, 1, -1):
    for j in xrange(1000, 1, -1):
        if palindrome(i * j) and i * j > maxpal:
            maxpal = i * j

print maxpal
