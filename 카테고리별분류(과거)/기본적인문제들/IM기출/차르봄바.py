# 차르봄바


# 방향배열
def boom(y, x, P):
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    virus = 0
    for i in range(4):
        for k in range(1, P + 1):
            ny = y + k * dir[i][0]
            nx = x + k * dir[i][1]
            if 0 <= ny < N and 0 <= nx < N:
                virus += MAP[ny][nx]
    return virus + MAP[y][x]



T = int(input())
for tc in range(1, T + 1):
    N, P = map(int, input().split())
    MAP = [list(map(int,input().split())) for _ in range(N)]
    max_virus = 0
    for i in range(N):
        for j in range(N):
            vir = boom(i, j, P)
            if vir >= max_virus:
                max_virus = vir
                mly, mlx = i, j
    print(f'#{tc} {max_virus}')



