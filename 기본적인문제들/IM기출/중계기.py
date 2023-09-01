# 중계기

from math import sqrt

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N + 1)]
    for i in range(N + 1):
        for j in range(N + 1):
            if MAP[i][j] == 2:
                sy = i
                sx = j

    max_r = 0

    for i in range(N + 1):
        for j in range(N + 1):
            if MAP[i][j] == 1:
                r = sqrt((sy - i) ** 2 + (sx - j) ** 2)
                if r >= max_r:
                    max_r = r

    if max_r % 1:
        max_r = int(max_r) + 1
    else:
        max_r = int(max_r)

    print(f'#{tc} {max_r}')