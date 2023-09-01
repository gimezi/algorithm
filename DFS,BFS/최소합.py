'''
그림처럼 NxN 칸에 숫자가 적힌 판이 주어지고, 각 칸에서는 오른쪽이나 아래로만 이동할 수 있다.
맨 왼쪽 위에서 오른쪽 아래까지 이동할 때, 
지나는 칸에 써진 숫자의 합계가 최소가 되도록 움직였다면 
이때의 합계가 얼마인지 출력하는 프로그램을 만드시오

[입력]
3
3
1 2 3
2 3 4
3 4 5
4
2 4 1 3
1 1 7 1
9 1 7 10
5 7 2 4
5
6 7 1 10 2
10 2 7 5 9
9 3 2 9 6
1 6 8 2 9
8 3 8 2 1


[출력]
#1 15
#2 18
#3 33
'''
## 강사님

dir = [(0, 1), (1, 0)]

def dfs(x, y, sumv):
    global result
    if sumv >= result:
        return
    if x == N - 1 and y == N - 1:
        if sumv < result:
            result = sumv
            return
    for dx, dy in dir:
        nx, ny = x + dx, y + dy
        if -1 < nx < N and -1 < ny < N:
            dfs(nx, ny, sumv + arr[nx][ny])
        

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    result = float('INF')
    dfs(0,0,arr[0][0])
    print(f'#{tc} {result}')















## 내꺼

# def DFS(y, x):
#     stack = [(y, x, MAP[y][x])]
#     dir = [(1, 0), (0, 1)]  # 오른쪽과 아래쪽
#     minv = float('INF')
#     while True:
#         cy, cx, score = stack.pop()
#         if cy == N - 1 and cx == N - 1:
#             if score < minv:
#                 minv = score
#             if stack:
#                 continue
#             else:
#                 break
#         else:
#             for k in range(2):
#                 ny, nx = cy + dir[k][0], cx + dir[k][1]
#                 if 0 <= ny < N and 0 <= nx < N:
#                     stack.append((ny, nx, score + MAP[ny][nx]))
    
#     return minv


# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     MAP = [list(map(int,input().split())) for _ in range(N)]
#     print(f'#{tc} {DFS(0,0)}')

