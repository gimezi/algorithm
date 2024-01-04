'''
BFS

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

dire = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def settingMAP():
    tmp = 2
    for i in range(N):
        for j in range(N):
            if MAP[i][j] == 1:
                MAP[i][j] = tmp
                q = deque([(i, j)])
                while q:
                    y, x = q.popleft()
                    for dy, dx in dire:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < N and 0 <= nx < N:
                            if MAP[ny][nx] == 1:
                                MAP[ny][nx] = tmp
                                q.append((ny, nx))
                tmp += 1

# minv는 현재까지의 최소거리
def find(y, x, ddang):
    q = deque([(0, y, x)])
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[y][x] = 1
    while q:
        dis, cy, cx = q.popleft()
        if MAP[cy][cx] and MAP[cy][cx] != ddang:
            return dis
        for dy, dx in dire:
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < N and 0 <= nx < N:
                # 물이면서 안들린 곳이라면
                if MAP[ny][nx] != ddang and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append([dis + 1, ny, nx])   
    return float('inf')            

N = int(input())
MAP = []
for _ in range(N):
    arr = list(map(int,input().split()))
    MAP.append(arr)

minval = float('inf')
settingMAP()
# print(find(2, 0, MAP[2][0]))

for i in range(N):
    for j in range(N):
        if MAP[i][j]:
            temp = find(i, j, MAP[i][j])
            if temp < minval:
                minval = temp
print(minval - 1)