'''
계단수: 인접한 모든 자리의 차이가 1인 수
ex) 45656
'''
n = int(input())
DP = [[0 for _ in range(10)] for _ in range(n)]

# 한자리 일 때는 하드 코딩
DP[0] = [1 for _ in range(10)]
DP[0][0] = 0

k = 1
while k < n:
  for i in range(10):
    if i == 0:
      DP[k][i] = DP[k - 1][1]
    elif i == 9:
      DP[k][i] = DP[k - 1][8]
    else:
      DP[k][i] = DP[k - 1][i - 1] + DP[k - 1][i + 1]
  k += 1
print(sum(DP[n - 1]) % 1000000000)