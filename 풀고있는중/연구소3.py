from collections import deque


dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N, M = map(int,input().split())
MAP = [list(map(int,input().split()))]

def time(starty, startx):
    que = deque([(starty, startx, 0)])   # 현재 위치, 시간, 바이러스 개수
    visited = [[0 for _ in range(N)]for _ in range(N)]
    visited[starty][startx] = 1
    while que:
        cy, cx, t= que.popleft()
        for dy, dx in dir:
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < N and 0 <= nx < N:
                if visited[ny][nx]== 0 and MAP[ny][nx] != 1:
                    pass
