# 벽 부수고 이동하기 2
'''
1번과 다르게 k개까지 뿌실 수 있음
'''

from collections import deque
import sys

dire = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def BFS(starty, startx):
    q = deque([(1, starty, startx, 0)])
    visited = [[[0 for _ in range(K + 1)] for _ in range(M)] for _ in range(N)]
    while q:
        dis, cy, cx, punch = q.popleft()
        if cy == N - 1 and cx == M - 1:
            return dis
        for dy, dx in dire:
            ny, nx = dy + cy, dx + cx
            if 0 <= ny < N and 0 <= nx < M:
                # 벽이라면
                if MAP[ny][nx] and punch < K and visited[ny][nx][punch + 1] == 0:
                    visited[ny][nx][punch + 1] = 1
                    q.append((dis + 1, ny, nx, punch + 1))
                # 벽이 아니라면
                elif MAP[ny][nx] == 0 and visited[ny][nx][punch] == 0:
                    visited[ny][nx][punch] = 1
                    q.append((dis + 1, ny, nx, punch))
    return -1

N, M, K = map(int, sys.stdin.readline().split())
MAP = []
for _ in range(N):
    MAP.append(list(map(int,sys.stdin.readline().strip())))

print(BFS(0, 0))