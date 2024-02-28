# 수학게임 페스티벌

from collections import deque

N = int(input())

def Lf(num):
    a = num // 1000
    b = num % 1000
    return b * 10 + a

def Rf(num):
    a = num // 10
    b = num % 10
    return b * 1000 + a

def Sf(num):
    if num:
        return num - 1
    else:
        return 9999

def Df(num):
    a = num * 2
    if a < 10000:
        return a
    else:
        return a % 10000


def BFS(start, end):
    que = deque([(start,'')])
    visited = set()

    while que:
        now, path = que.popleft()
        if now == end:
            return path            

        if now not in visited:
            visited.add(now)
            if 0 <= Df(now) <= 9999:
                que.append((Df(now),path + 'D'))

            if 0 <= Sf(now) <= 9999:
                que.append((Sf(now),path+'S'))    

            if 0 <= Lf(now) <= 9999:
                que.append((Lf(now),path+'L'))

            if 0 <= Rf(now) <= 9999:
                que.append((Rf(now),path+'R'))  


for _ in range(N):
    A, B = map(int, input().split())
    print(BFS(A, B))