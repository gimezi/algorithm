# 코스타그램 SWEA
from collections import deque

N = int(input())
M = int(input())
arr = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
coco = int(input())

def BFS(start):
    cnt = 0
    que = deque([(start, 0)])
    visited = [0 for _ in range(N + 1)]
    visited[start] = 1
    while que:
        now, level = que.popleft()
        print(now, level)
        if level:
            cnt += 1
        if arr[now]:
            for next1 in arr[now]:
                if not visited[next1]:
                    visited[next1] = 1
                    que.append((next1, level + 1))   
    return cnt
print(BFS(coco))