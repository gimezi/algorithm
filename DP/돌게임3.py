# 9657 돌게임3

'''
돌이 N개 있고, 한번에 1, 3, 4개 가져갈 수있다
마지막 돌을 가져가면 이김

내꺼 -1, -3, -4가 다 이길수가 없다면, 지는거임
하나라도 길이 있다면 이김!
'''

# N = int(input())
# if N < 4:
#     if N == 2:
#         print('CY')
#     else:
#         print('SK')
# else:
#     DP = [0 for _ in range(N + 1)]
#     DP[2] = 1   # 1이 CY
#     DP[1], DP[3], DP[4] = 2,2,2 # 2가 sk

#     def dol(n):
#         if DP[n]:
#             return DP[n]
#         else:
#             if n >= 5:
#                 if dol(n - 1) == dol(n - 3) == dol(n - 4) == 2:
#                     DP[n] = 1
#                 else:
#                     DP[n] = 2
#             return DP[n]
#     if dol(N) ==  1:
#         print('CY')
#     elif dol(N) == 2:
#         print('SK')


















# N = int(input())

# # dp[i]는 돌이 i개 남았을 때 이기는 사람 // True면 상근 승, False면 창영 승
# dp = [False] * (N + 1)

# for i in [1, 3, 4]:
#     if i <= N:
#         dp[i] = True

# for i in range(5, N + 1):
#     dp[i] = not (dp[i-1] and dp[i-3] and dp[i-4])

# print("SK" if dp[N] else "CY")

    
