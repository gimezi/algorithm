# 17070번 파이프 옮기기

'''
유현이가 새 집으로 이사했다. 새 집의 크기는 NxN의 격자판으로 나타낼 수 있고, 
1x1크기의 정사각형 칸으로 나누어져 있다. 각각의 칸은 (r, c)로 나타낼 수 있다. 
여기서 r은 행의 번호, c는 열의 번호이고, 행과 열의 번호는 1부터 시작한다. 
각각의 칸은 빈 칸이거나 벽이다.
오늘은 집 수리를 위해서 파이프 하나를 옮기려고 한다. 
파이프는 2개의 연속된 칸을 차지하는 크기이다.

파이프를 밀 수 있는 방향은 총 3가지가 있으며, →, ↘, ↓ 방향이다. 
파이프는 밀면서 회전시킬 수 있다.

첫째 줄에 파이프의 한쪽 끝을 (N, N)으로 이동시키는 방법의 수를 출력한다. 
이동시킬 수 없는 경우에는 0을 출력한다. 
방법의 수는 항상 1,000,000보다 작거나 같다.

[입력]
3
0 0 0
0 0 0
0 0 0


6
0 0 0 0 0 0
0 1 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0


[출력]
1

13
'''
'''
현재 상태에 따라 갈 수 있는 방향이 달라진다
BFS 자꾸 시간초과남..ㅜㅜ

DP...해야겠지.....
'''

# 방향: 가로 0, 세로 1, 대각선 2
print(((1,2))+((3,4)))

# N = int(input())
# MAP = [list(map(int,input().split())) for _ in range(N)]
# DP = [[() for _ in range(N)] for _ in range(N)]

# def find(y, x):
#     if DP[y][x]:
#         return DP[y][x]
#     DP[y][x] = 





















# #재귀함수를 이용해 모든 경우의 수 구하기
# def recursive(y, x, shape):  # 파이프의 오른쪽 끝 위치와 현재 파이프의 상태를 전달하고 파이프를 이동시킬 위치를 검사하는 함수
#     global ans
#     # 5개의 조건문이 참인지 순차적으로 검토(파이프를 이동시킬 위치를 검토)
#     # 종료 조건
#     if y > n or x > n:  # 파이프의 위치가 집의 범위를 넘어선 경우
#         return
#     if y == n and x == n:  # 파이프가 목적지에 도착한 경우(이 경우 경우의 수를 카운트하고 다음 조건문으로 넘어가 조건문이 참이 되더라도 어차피 재귀 호출의 결과 파이프의 위치가 집의 범위를 넘어서게 되므로 함수가 종료됨))
#         ans += 1
#     if home[y][x+1] == 0 and (shape == 0 or shape ==2):  # 기준점의 오른쪽이 벽이 아니고 현재 상태가 가로거나 대각선인 경우 재귀함수 호출(가로로 이동)
#         recursive(y, x+1, 0)
#     if home[y+1][x] == 0 and (shape == 1 or shape == 2):  # 기준점의 아래쪽이 벽이 아니고 현재 상태가 세로거나 대각선인 경우(세로로 이동)
#         recursive(y+1, x, 1)
#     if home[y+1][x] == 0 and home[y][x+1] == 0 and home[x+1][y+1] ==0:  # 기준점의 오른쪽, 아래쪽 대각선 아래가 모두 벽이 아닌 경우(대각선으로 이동)
#         recursive(y+1, x+1, 2)

# n = int(input())
# home = [[0 for _ in range(18)] for _ in range(18)]  # 18x18배열
# # 3 <= n <= 16이므로 최댓값일 경우보다 2칸 여유있게 배열을 만든다.
# for i in range(1, n+1):
#     row = list(map(int, input().split())) # 집의 구조를 한 줄씩 입력받아서
#     for j in range(1, n+1): # home을 1부터 n행과 n열까지만 채우기
#         home[i][j] = row[j-1]

# ans = 0  # 구하고자 하는 경우의 수
# recursive(1, 2, 0)  # 파이프의 초기 위치와 상태는 고정조건
# print(ans)





# ## 시간 초과남ㅜㅜㅠㅠㅠㅠ
# from collections import deque
# import sys
# input = sys.stdin.readline

# N = int(input())
# dirs = [[(0, 1), (0, 0), (1, 1)], [(0, 0), (1, 0), (1, 1)], [(0, 1), (1, 0), (1, 1)]]
# MAP = [list(map(int,input().split())) for _ in range(N)]
# def find(sy, sx, n):        # 시작점 좌표와 방향, (0,1,0)
#     que = deque([(sy, sx, n, '(0, 1)')])
#     cnt = 0
#     if MAP[N-1][N-1] == 1:
#         return 0
#     while que:
#         cy, cx, dire, visited = que.popleft()
#         for dy, dx in dirs[dire]:
#             ny = cy + dy
#             nx = cx + dx
#             if 0 <= ny < N and 0 <= nx < N and MAP[ny][nx] == 0 and str((ny, nx)) not in visited:
#                 if dy and dx:   # 대각선방향일때, 
#                     if MAP[ny- 1][nx]== 0 and MAP[ny][nx - 1] == 0:
#                         if ny == N - 1 and nx == N - 1:     # 끝까지 다 오면 = 도착하면,
#                             cnt += 1
#                         que.append((ny, nx, 2, visited + str((ny, nx))))
#                 elif dy:
#                     if ny == N - 1 and nx == N - 1:     # 끝까지 다 오면 = 도착하면,
#                         cnt += 1
#                     que.append((ny, nx, 1, visited + str((ny, nx))))
#                 else:
#                     if ny == N - 1 and nx == N - 1:     # 끝까지 다 오면 = 도착하면,
#                         cnt += 1
#                     que.append((ny, nx, 0, visited + str((ny, nx))))
#     return cnt

# print(find(0, 1, 0))
