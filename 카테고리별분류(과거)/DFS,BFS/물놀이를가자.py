# 물놀이를 가자

'''
땅으로 표현된 모든 칸에 대해서, 
어떤 물인 칸으로 이동하기 위한 최소 이동 횟수를 구하고 
모든 이동 횟수의 합을 출력하는 프로그램을 작성하라.

3
2 3
WLL
LLL
3 2
WL
LL
LW
4 5
LLLWW
WWLLL
LLLWL
LWLLL

#1 9
#2 4
#3 15

'''
'''
최소 거리니까 BFS를 써야겠네

'''

# 물에서 부터 시작해서 하나하나 늘리는 방법

from collections import deque

dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int,input().split())
    check = [[-1 for _ in range(M)] for _ in range(N)]
    q = deque()

    for i in range(N):
        t = input()
        for j in range(M):
            if t[j] == 'W':
                q.append((i,j))
                check[i][j] = 0
    result = 0
    
    while q:
        x, y = q.popleft()
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and check[nx][ny] == -1:
                q.append((nx,ny))
                check[nx][ny] = check[x][y] + 1
                result += check[nx][ny]
    print(f'#{tc} {result}')




## 이건 물 ~ 물까지 가면서 각각의 최소경로를 업데이트 했었음

# from collections import deque

# def findwater(y, x):        # W의 위치에서 W를 찾는 함수
#     que = deque([(y, x, 0)])
#     dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#     visited = [[0 for _ in range(M)] for _ in range(N)]
#     visited[y][x] = 1
#     sumarr[y][x] = 0
#     while que:
#         cy, cx, level = que.popleft()
#         if MAP[cy][cx] == 'W' and visited[cy][cx] == 0:      # 다른 물을 찾으면 스탑
#             return
#         for dy, dx in dir:
#             ny, nx = cy + dy, cx + dx   
#             if 0 <= ny < N and 0 <= nx < M:
#                 if visited[ny][nx] == 0: 
#                     sumarr[ny][nx] = min(sumarr[ny][nx], level + 1)
#                     que.append((ny, nx, level + 1))
#                     visited[ny][nx] = 1
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int,input().split())
#     MAP = [list(input()) for _ in range(N)]
#     sumarr = [[float('INF') for _ in range(M)] for _ in range(N)]
#     water = []
#     for i in range(N):
#         for j in range(M):
#             if MAP[i][j] == 'W':
#                 water.append((i, j))
#     for y, x in water:
#         findwater(y,x)
#     result = 0
#     for arr in sumarr:
#         result += sum(arr)
#     print(f'#{tc} {result}')





# # DP방식(구글링)
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int,input().split())
#     MAP = [list(input()) for _ in range(N)]
#     DP = [[float('INF') for _ in range(M)] for _ in range(N)]
#     ans = 0
#     # ↘ 방향
#     for i in range(N):
#         for j in range(M):
#             if MAP[i][j] == 'W':
#                 DP[i][j] = 0
#             else:
#                 if i:
#                     DP[i][j] = min(DP[i - 1][j] + 1, DP[i][j])
#                 if j:
#                     DP[i][j] = min(DP[i][j - 1] + 1, DP[i][j])
    
#     # ↖ 방향
#     for i in range(N - 1, -1, -1):
#         for j in range(M-1, -1 ,-1):
#             if MAP[i][j] == 'L':
#                 if not j == M - 1:
#                     DP[i][j] = min(DP[i][j + 1] + 1, DP[i][j])
#                 if not i == N - 1:
#                     DP[i][j] = min(DP[i + 1][j] + 1, DP[i][j])
#                 if DP[i][j] == float('INF'):
#                     continue
#                 ans += DP[i][j]
#     print(ans)




# from collections import deque
# def findwater(y, x):        # 현재위치가 주어졌을 때, W까지의 최소거리를 구하는 함수
#     que = deque([(y, x, 0)])
#     visited = [(y, x)]
#     dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#     while que:
#         cy, cx, level = que.popleft()
#         if MAP[cy][cx] == 'W':      # 종료조건
#             return level
#         for dy, dx in dir:
#             ny, nx = cy + dy, cx + dx
#             if 0 <= ny < N and 0 <= nx < M:
#                 if (ny, nx) not in visited:
#                     que.append((ny, nx, level + 1))
#                     visited.append((ny, nx))
    

# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int,input().split())
#     MAP = [list(input()) for _ in range(N)]
#     result = 0 
#     for i in range(N):
#         for j in range(M):
#             result += findwater(i, j)
#     print(f'#{tc} {result}')
