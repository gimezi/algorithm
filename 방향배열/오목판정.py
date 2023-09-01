# 11315번 오목판정

position1 = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]
position2 = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]
position3 = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
position4 = [(0, 0), (-1, 1), (-2, 2), (-3, 3), (-4, 4)]

def iden_omok1(a, b):
    arr = []
    for i, j in position1:
        new_a = a + i
        new_b = b + j
        if 0 <= new_a < N and 0 <= new_b < N:
            arr.append(omok[new_a][new_b])
    if arr == ['o', 'o', 'o', 'o', 'o']:
        return True
    

def iden_omok2(a, b):
    arr = []
    for i, j in position2:
        new_a = a + i
        new_b = b + j
        if 0 <= new_a < N and 0 <= new_b < N:
            arr.append(omok[new_a][new_b])
    if arr == ['o', 'o', 'o', 'o', 'o']:
        return True
    

def iden_omok3(a, b):
    arr = []
    for i, j in position3:
        new_a = a + i
        new_b = b + j
        if 0 <= new_a < N and 0 <= new_b < N:
            arr.append(omok[new_a][new_b])
    if arr == ['o', 'o', 'o', 'o', 'o']:
        return True
    

def iden_omok4(a, b):
    arr = []
    for i, j in position4:
        new_a = a + i
        new_b = b + j
        if 0 <= new_a < N and 0 <= new_b < N:
            arr.append(omok[new_a][new_b])
    if arr == ['o', 'o', 'o', 'o', 'o']:
        return True
    




T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    omok = [list(input()) for _ in range(N)]
    check = 'NO'
    for i in range(N):
        for j in range(N):
            if iden_omok1(i, j) == True:
                check = 'YES'
            elif iden_omok2(i, j) == True:
                check = 'YES'
            elif iden_omok3(i, j) == True:
                check = 'YES'
            elif iden_omok4(i, j) == True:
                check = 'YES'
    

    print(f'#{tc} {check}')