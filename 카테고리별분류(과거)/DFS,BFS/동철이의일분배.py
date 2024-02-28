# SWEA 동철이의 일 분배

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    p = [list(map(int,input().split())) for _ in range(N)]
    percent = 0     # 계산용 퍼센트
    visited = [0 for _ in range(N)]

    def DFS(n, pe):
        global percent
        if pe <= percent:
            return
        if n == N - 1:
            percent = pe
            return 
        for k in range(N):
            if visited[k] == 0:
                visited[k] = 1
                DFS(n + 1, pe * p[n + 1][k] / 100)
                visited[k] = 0

    for i in range(N):
        visited[i] = 1
        DFS(0, p[0][i] / 100)
        visited[i] = 0 

    ans = percent * 100
    print(f'#{tc}','{:.6f}'.format(ans))