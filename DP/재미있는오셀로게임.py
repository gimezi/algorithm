# SWEA 재미있는 오셀로 게임 
'''

1
4 12
1 2 1
1 1 2
4 3 1
4 4 2
2 1 1
4 2 2
3 4 1
1 3 2
2 4 1
1 4 2
4 1 2
3 1 2
'''

def f(i, j, bw, N):
    board[i][j] = bw
    for di, dj in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        ni, nj = i + di, j + dj
        tmp = []
        # 보드 내부이고 다른 색이면
        while 0 <= ni < N and 0 <= nj < N and board[ni][nj] == op[bw]:
            tmp.append((ni, nj))
            ni, nj = ni + di, nj + dj
        # 보드 내부이고 같은 색이면
        if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == bw:
            for p, q in tmp:
                board[p][q] = bw    

B = 1
W = 2
op = [0, 2, 1]

T = int(input())
for tc in range(1, T  + 1):
    N, M = map(int, input().split())
    play = [list(map(int, input().split())) for _ in range(M)]
    board = [[0] * N for _ in range(N)]

    board[N //2 - 1][N //2 - 1] = W
    board[N //2 - 1][N // 2] = B
    board[N // 2][N //2 - 1] = B
    board[N // 2][N // 2] = W
    for col, row, bw in play:
        f(row - 1, col - 1, bw, N)  # 이거 돌면 돌이 다 놓임
    # 보드위의 흑/백돌의 개수를 출력
    bcnt = wcnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == B:
                bcnt += 1
            elif board[i][j] == W:
                wcnt += 1

    print(f'#{tc} {bcnt} {wcnt}')
    