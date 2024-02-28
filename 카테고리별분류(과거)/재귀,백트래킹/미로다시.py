# SWEA 미로

T = int(input())


def BFS(sy, sx):
    que = [(sy, sx)]
    dire = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[sy][sx] = 1

    while que:
        cy, cx = que.pop(0)
    
        for i in range(4):
            dy = dire[i][0]
            dx = dire[i][1]
            ny = cy + dy
            nx = cx + dx
            if 0 <= ny < N and 0 <= nx < N:
                if arr[cy][cx] == 3:
                    return 1
                if arr[ny][nx] == 0 and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    que.append((ny, nx))

    return 0
        

for tc in range(1, T  + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                sy, sx = i, j
    
    print(BFS(sy, sx))

