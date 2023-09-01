# 사각형 그리기 게임

'''
사각형을 그리는 데에는 아래 두가지 조건을 충족해야만 한다. 
[1] 특정 좌표를 기준으로, "우측 하단"의 방향으로 사각형을 그릴 수 있다. 
[2] 왼쪽 상단 좌표의 값과 우측 하단 좌표의 값이 동일해야 한다. 
'''
def sqr(y, x):
    max_sqr = 0
    cnt = 0
    for i in range(N):
        for j in range(N):
            ny = y + i
            nx = x + j
            if 0 <= ny < N and 0 <= nx < N:
                if MAP[ny][nx] == MAP[y][x]:
                    S = (ny - y + 1) * (nx - x + 1)
                    if S > max_sqr:
                        cnt = 1
                        max_sqr = S
                    elif S == max_sqr:
                        cnt += 1
    return [max_sqr, cnt]




T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    max_s = 0
    max_cnt = 0
    for i in range(N):
        for j in range(N):
            sqrm, cnt = sqr(i,j)
            if sqrm > max_s:
                max_s = sqrm
                max_cnt = cnt
            elif sqrm == max_s:
                max_cnt += cnt
    print(f'#{tc} {max_cnt}')

    

    