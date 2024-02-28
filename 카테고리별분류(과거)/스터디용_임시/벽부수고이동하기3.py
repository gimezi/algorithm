# 벽 부수고 이동하기 3
'''
2번이랑 똑같은데 낮과 밤이 있고
낮에만 이동 가능.
처음은 낮 = dis가 1일 때 낮, 2일 때 밤, 3일 때 낮...
즉, dis % 2 == 1이면 낮, 0이면 밤이다
'''

from collections import deque
import sys

dire = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def BFS(starty, startx):
    
    q = deque([(1, starty, startx, 0)])
    visited = [[[0 for _ in range(K + 1)] for _ in range(M)] for _ in range(N)]
    visited[starty][startx] = [1 for _ in range(K + 1)]
    while q:
        # print(q)
        dis, cy, cx, punch = q.popleft()
        if cy == N - 1 and cx == M - 1:
            return dis
        for dy, dx in dire:
            ny, nx = dy + cy, dx + cx
            if 0 <= ny < N and 0 <= nx < M:
                # 낮일 때
                if dis % 2:
                    # 벽이 있다면 -> 부시고 진행
                    if MAP[ny][nx] == 1 and punch < K and visited[ny][nx][punch + 1] == 0:
                        visited[ny][nx][punch + 1] = 1
                        q.append((dis + 1, ny, nx, punch + 1))
                    # 벽이 없다면 그냥 진행
                    elif MAP[ny][nx] == 0 and visited[ny][nx][punch] == 0:
                        visited[ny][nx][punch] = 1
                        q.append((dis + 1, ny, nx, punch))
                # 밤이라면
                else:
                    # 벽이 있다면 -> 한번 제자리에서 기다려보자
                    if MAP[ny][nx] == 1 and punch < K and visited[ny][nx][punch + 1] == 0:
                        q.append((dis + 1, cy, cx, punch))
                    elif MAP[ny][nx] == 0 and visited[ny][nx][punch] == 0:
                        visited[ny][nx][punch] = 1
                        q.append((dis + 1, ny, nx, punch))
    return -1

N, M, K = map(int, sys.stdin.readline().split())
MAP = []
for _ in range(N):
    MAP.append(list(map(int,sys.stdin.readline().strip())))

print(BFS(0, 0))