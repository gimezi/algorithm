n = int(input())
stairs = [0]
for _ in range(n):
  stairs.append(int(input()))


DP = [[0 for _ in range(n + 1)] for _ in range(2)]
if n >= 2:
  # 1번, 2번칸은 하드코딩 해버리자
  DP[0][1] = 0
  DP[1][1] = stairs[1]
  DP[0][2] = stairs[2]
  DP[1][2] = stairs[1] + stairs[2]

  for k in range(3, n + 1):
    DP[0][k] = max(DP[0][k - 2], DP[1][k - 2]) + stairs[k]
    DP[1][k] = DP[0][k - 1] + stairs[k]

  print(max(DP[0][n], DP[1][n]))
else:
  print(stairs[1])
