# 구간합 구하기5
'''
https://www.acmicpc.net/problem/11660

NxN개의 수가 NxN 크기의 표에 채워져 있다. 
(x1, y1)부터 (x2, y2)까지 합을 구하는 프로그램을 작성하시오. (x, y)는 x행 y열을 의미한다.

[입력]
4 3
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7
2 2 3 4
3 4 3 4
1 1 4 4

[출력]
27
6
64
'''


# M의 값이 매우매우 커질수도있으므로 input도 신경써야함
import sys
input = sys.stdin.readline

## DP를 써보자
N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

# DP 행렬부터 구해보자 DP[i][j]는 (1,1)부터 (i,j)까지의 합
DP = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        DP[i][j] = DP[i][j - 1] + DP[i -1][j] - DP[i - 1][j - 1] + arr[i - 1][j - 1]

for _ in range(M):
    x1, y1, x2, y2 = map(int,input().split())
    result = DP[x2][y2] - DP[x1 - 1][y2] - DP[x2][y1 - 1] + DP[x1 - 1][y1 - 1]
    print(result)
    











# # 시간초과가 나버림
# N, M = map(int,input().split())
# arr = [list(map(int,input().split())) for _ in range(N)]
# goals = [list(map(int,input().split())) for _ in range(M)]

# # 누적합 행렬부터 구해보자
# sumarr = [[0 for _ in range(N)] for _ in range(N)]
# for i in range(N):
#     for j in range(N):
#         sumarr[i][j] = sum(arr[i][:j+1])

# # 답을 구해보자
# for x1, y1, x2, y2 in goals:
#     result = 0
#     if x1 == x2 and y1 == y2:
#         result += arr[x1 - 1][y1 - 1]
#     elif x1 != 1 and y1 != 1:
#         for y in range(y1 - 1, y2):
#             result += sumarr[y][x2 - 1]
#             result -= sumarr[y][x1 - 2]
#     elif x1 == 1 and y1 == 1:
#         for y in range(y2):
#             result += sumarr[y][x2 - 1]
#     elif x1 == 1:
#         for y in range(y1 - 1, y2):
#             result += sumarr[y][x2 - 1]
#     else:
#         for y in range(y2):
#             result += sumarr[y][x2 - 1]
#             result -= sumarr[y][x1 - 2]

#     print(result)




# '''
# N, M = map(int,input().split())
# MAP = [list(map(int,input().split())) for _ in range(N)]
# sum_map = [[0 for _ in range(N)] for _ in range(N)]             # 행별로 누적 합을 담을 MAP
# for i in range(N):
#     sum_map[i][0] = MAP[i][0]
#     for j in range(1, N):
#         sum_map[i][j] = sum_map[i][j - 1] + MAP[i][j]

# for _ in range(M):
#     x1, y1, x2, y2 = map(int,input().split())
#     result = 0
#     for k in range(y1, y2 - 1):
#         result += sum_map[k][x2 - 1]
#         result -= sum_map[k][x1 - 1]
#         result += MAP[k][x1 - 1]

#     print(result)
# '''