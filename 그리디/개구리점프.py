# 개구리 점프

'''
4 2
1 5 2
3 7 4
7 9 1
10 13 4
1 3
1 4


1
0
'''
# from collections import deque

# def find(n, goal): 
#     que = deque([n])
#     visited = [0 for _ in range(N + 1)]
#     visited[n] = 1
#     while que:
#         now = que.popleft()
#         minv = namu[now - 1][1]
#         maxv = namu[now - 1][2]
#         if now == goal:
#             return 1
#         if namu[now - 2][2] > minv and visited[namu[now - 2][0]] == 0:
#             visited[namu[now - 2][0]] = 1
#             que.append(now - 1)
#             visited[namu[now - 2][0]] = 0

#         if namu[now][2] < maxv and visited[namu[now][0]] == 0:
#             visited[namu[now][0]] = 1
#             que.append(now + 1)
#             visited[namu[now][0]] = 0
#     return 0

# N, Q = map(int,input().split())
# namu = []
# for i in range(N):
#     a = list(map(int,input().split()))
#     a.insert(0,i + 1)
#     namu.append(a)      # [[1, 1, 5, 2], [2, 3, 7, 4], [3, 7, 9, 1], [4, 10, 13, 4]]
# namu.sort(key= lambda x:x[1])   # 시작점 기준으로 sort
# for _ in range(Q):
#     a, b = map(int, input().split())
#     print(find(a,b))










# N, Q = map(int,input().split())

# tong = []

# for k in range(N):
#     a = list(map(int,input().split()))
#     a.insert(0, k + 1)
#     tong.append(a)

# tong.sort(key= lambda x:x[1])
# startarr = [i for i in range(N + 1)]

# i = 1
# while i < N:
#     if tong[i - 1][2] >= tong[i][1]:
#         if startarr[tong[i][0]] == tong[i][0]:
#             startarr[tong[i][0]] = startarr[tong[i - 1][0]]
#     i += 1

# for _ in range(Q):
#     a, b = map(int,input().split())
#     if startarr[a] == startarr[b]:
#         print(1)
#     else:
#         print(0)







# Union Find로
import sys
input = sys.stdin.readline

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    parent[b] = a

N, Q = map(int, input().split())
tong = []

for k in range(N):
    a, b, c = map(int, input().split())
    tong.append((a, b, c, k))

tong.sort()

parent = [i for i in range(N)]

nowstart, nowend, nowindex = tong[0][0], tong[0][1], tong[0][3]
for i in range(1, N):
    nextstart, nextend, nextindex = tong[i][0], tong[i][1], tong[i][3]
    if nowstart <= nextstart <= nowend:
        union(nowindex, nextindex)
        if nextend >= nowend:
            nowstart, nowend, nowindex = nextstart, nextend, nextindex
    else:
        nowstart, nowend, nowindex = nextstart, nextend, nextindex

for _ in range(Q):
    a, b = map(int, input().split())
    if parent[a - 1] == parent[b - 1]:
        print(1)
    else:
        print(0)