def tri_num(n):
    return n * (n+1) / 2

def pent_num(n):
    return n * (3*n-1) / 2

def hex_num(n):
    return n * (2*n-1)

nArr = [286, 165, 143]
valArr = [tri_num(nArr[0]), pent_num(nArr[1]), hex_num(nArr[2])]

while not (valArr[0] == valArr[1] == valArr[2]):
    nArr[valArr.index(min(valArr))] += 1

    valArr = [tri_num(nArr[0]), pent_num(nArr[1]), hex_num(nArr[2])]

print valArr[0]
