# 백준 16236번 아기상어

'''
아기상어 초기 크기: 2
1초에 상하좌우 한칸씩
자기보다 작은 물고기만 먹을 수 있다.
크기가 같은 물고기는 못 먹지만, 지나갈 수는 있다.

더이상 먹을 수 있는 게 없으면 엄마를 불러요
1마리면 먹으러가요
먹을 수 있는 물고기가 1마리보다 많으면 가장 가까운걸 먹으러가요(= BFS)
거리가 가까운게 여러개라면 가장 위에, 가장 왼쪽에 있는걸 먹으러간다
(상-좌-우-하 순서)
상어는 자신의 크기와 같은 수의 물고기를 먹을때마다 크기가 1증가한다

9 = 상어의 위치
물고기를 잡아먹을 수 있는 시간을 출력

[tc 1]
3
0 0 0
0 0 0
0 9 0

0

[tc 2]
3
0 0 1
0 0 0
0 9 0


3
'''
from collections import deque

dir = [(0, -1), (-1, 0), (1, 0), (0, 1)]    # 상 좌 우 하
N = int(input())
ocean = [list(map(int,input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if ocean[i][j] == 9:
            sharky = i
            sharkx = j
sharksize = 2
fish = 0
time = 0

def eat(y, x, t):  # 시작점, 시간
    global sharksize, fish, time
    que = deque([(y, x, t)])
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[y][x] = 1
    while que:
        cy, cx, t = que.popleft()
        print(cy, cx, t, sharksize)
        if ocean[cy][cx]:
            if ocean[cy][cx] < sharksize:
                sharksize += 1
                fish += 1
                time += t
                ocean[cy][cx] = 0
                left = 0
                for i in range(N):
                    left += sum(ocean[i])
                print(left, ocean, time, fish)
                if left == 9:
                    if fish:
                        return time
                    else:
                        return 0
                else:
                    eat(cy, cx, t)
                
                break
        for dy, dx in dir:
            ny = cy + dy
            nx = cx + dx
            if 0 <= ny < N and 0 <= nx < N:
                if visited[ny][nx] == 0 and ocean[ny][nx] <= sharksize:
                    visited[ny][nx] = 1
                    que.append((ny, nx, t + 1))
    

        

print(eat(sharky, sharkx, 0))
