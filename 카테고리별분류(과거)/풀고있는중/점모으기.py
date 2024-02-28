# 점 모으기

N, M = map(int,input().split())

# x, y 들
xs = []
ys = []
for _ in range(M):
    a, b = map(int,input().split())
    xs.append(a)
    ys.append(b)
xs.sort()
ys.sort()

# 중앙값 구하기
x, y = xs[M//2], ys[M//2]
result = 0
for i in xs:
    result +=  abs(i - x)
for j in ys:
    result += abs(j - y)

print(result)






# # 메모리 초과 남
# N, M = map(int,input().split())
# sq = [[0 for _ in range(N)] for _ in range(N)]
# for _ in range(M):
#     a, b = map(int,input().split())
#     for i in range(N):
#         for j in range(N):
#             sq[i][j] += abs(i - a + 1)
#             sq[i][j] += abs(j - b + 1)

# min = float('inf')
# for i in range(N):
#     for j in range(N):
#         if min > sq[i][j]:
#             min = sq[i][j]

# print(min)