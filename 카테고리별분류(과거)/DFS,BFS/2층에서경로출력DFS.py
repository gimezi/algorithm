# 2층에서 경로출력 DFS
# 경로에서 2단계에 가면 경로 출력
'''
input data

9
0 1 1 0 0 0 0 0 0
0 0 0 1 1 1 0 0 0
0 0 0 0 0 0 1 1 1
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0


'''

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
visited = [0] * 3


def DFS(now, level):
    global visited
    visited[level] = str(now)
    if level == 2:
        print(''.join(visited))
    for i in range(N):
        if arr[now][i] == 1:
            DFS(i, level + 1)

DFS(0, 0)
