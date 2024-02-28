#일곱난쟁이
#난쟁이들 키 받기
a = []
for i in range(0,9):
    a.append(int(input()))

# 전체 난쟁이들의 합
S = 0
for i in range(0,9):
    S = S + a[i]

# 두명 더해서 N이 되면 걔네는 빼기
N = S - 100

itsyou = []

for i in range(0,9):
    for j in range(0,9):
        if a[i] != a[j]:
            if a[i] + a[j] == N:
                itsyou.append(i)
                itsyou.append(j)

p = itsyou[0]
q = itsyou[1]

del a[p]
del a[q-1]

a.sort()

for i in range(0,7):
    print(a[i])