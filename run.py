import sys
from AHP import *

try:
    cFile = sys.argv[1]
    dFile = sys.argv[2]
except:
    print("INVALID INPUT")
    sys.exit()

session = AHP(cFile, dFile)

session.criList = []
session.degList = []

deg = session.degCount # 4
N = session.criCount # 9

print("Degree = " + str(deg * 2 + 1))
print("Criteria = " + str(N))

for i in range(0, N):
    for j in range(i + 1, N):
        print('Enter which criterion (A or B) is relatively more important:')
        print('A. ' + session.criList[i])
        print('B. ' + session.criList[j])
        char = str(input())
        print()
        print('How would you describe this relative importance? ')
        for k in range(1, 8):
            print('[' + str(k) + '] ' + session.degList[k])
        deg = int(input())
        if(char == 'A'):
            session.compMat[i][j] = AHP.getTFN(deg)
            session.compMat[j][i] = AHP.invTFN(deg)
        else:
            session.compMat[i][j] = AHP.invTFN(deg)
            session.compMat[j][i] = AHP.getTFN(deg)
        print()

print('Fuzzy comparison matrix:')
for x in range(N):
    for y in range(N):
        print(str(session.compMat[x][y]), end = ' ')
    print()
    print()

print('Fuzzy geometric mean for each row:')
r = []
for x in range(N):
    p1, p2, p3 = 1, 1, 1
    for y in range(N):
        p1, p2, p3 = p1 * session.compMat[x][y][0], p2 * session.compMat[x][y][1], p3 * session.compMat[x][y][2]
    p1, p2, p3 = p1**(1/N), p2**(1/N), p3**(1/N)
    r.append((p1, p2, p3))
    print(session.criList[x] + " = " + str(r[x]))
print() 

print('Relative fuzzy weight for each criterion:')
f = []
l, m, u = 0, 0, 0
for i in range(N):
    l, m, u = l + r[i][0], m + r[i][1], u + r[i][2]
for i in range(N):
    f.append((r[i][0] / u, r[i][1] / m, r[i][2] / l))
    print(session.criList[i] + " = " + str(f[i]))
print()

print('Defuzzification by COA method:')
d = []
for i in range(N):
    d.append((f[i][0] + f[i][1] + f[i][2]) / 3)
for i in range(N):
    print(session.criList[i] + " = " + str(d[i]))
print()

print('Normalized weights for each criterion:')
w = []
s = 0
for i in range(N):
    s = s + d[i]
for i in range(N):
    w.append(d[i] / s)
for i in range(N):
    print(session.criList[i] + " = " + str(w[i]))
print()