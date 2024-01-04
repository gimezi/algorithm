'''
10
1 1 1 0 0 0 0 1 1 1
1 1 1 1 0 0 0 0 1 1
1 0 1 1 0 0 0 0 1 1
0 0 1 1 1 0 0 0 0 1
0 0 0 1 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 0 0 0 0
0 0 0 0 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0
'''
from collections import deque
# minv는 현재까지의 최소거리
def find(y, x, minv):
    q = deque([0, (y, x)])
    visited = [[0 for _ in range(N)] for _ in range(N)]
    while q:
        pass


N = int(input())
MAP = []
for _ in range(N):
    arr = list(map(int,input().split()))
    MAP.append(arr)

minval = float('inf')

for i in range(N):
    for j in range(N):
        if MAP[i][j]:
            find(i, j, minval)

print(minval)