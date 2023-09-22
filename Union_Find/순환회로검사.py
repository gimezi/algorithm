# 순환회로검사
# Union - Find 기초기초기초
'''
노드의 개수와 인접행렬 형태를 받고,
순환회로가 존재한다면 WARNING, 아니라면 STABLE을 출력
'''

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
parent = [i for i in range(N + 1)]

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        print('사이클발생')
        return
    
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

is_true = True
for y in range(N):
    for x in range(N):
        if arr[y][x]:
            if find(y) != find(x):
                union(x, y)
                arr[y][x] = 0
                arr[x][y] = 0
            else:
                is_true = False

if is_true:
    print('STABLE')
else:
    print('WARNING')
