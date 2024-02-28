## 전자카트
# 완전탐색 + 순열
'''
사무실에서 출발해 각 구역을 한 번씩만 방문하고 사무실로 돌아올 때의 최소 배터리 사용량을 구하시오.
각 구역을 이동할 때의 배터리 사용량은 표로 제공되며, 1번은 사무실을, 2번부터 N번은 관리구역 번호이다.
두 구역 사이도 갈 때와 올 때의 경사나 통행로가 다를 수 있으므로 배터리 소비량은 다를 수 있다.
N이 3인 경우 가능한 경로는 1-2-3-1, 1-3-2-1이며 각각의 배터리 소비량은 다음과 같이 계산할 수 있다.
e[1][2]+e[2][3]+e[3][1] = 18+55+18 = 91
e[1][3]+e[3][2]+e[2][1] = 34+7+48 = 89


[입력]
3
3
0 18 34
48 0 55
18 7 0
4
0 83 65 97
82 0 78 6
19 19 0 82
6 34 94 0
5
0 9 26 85 42
14 0 84 31 27
58 88 0 16 46
83 61 94 0 17
40 71 24 38 0

[출력]
#1 89
#2 96
#3 139
'''
'''
경로 종류는 순열로 구하고, 
구해진 순열에 따라 더하는것도 해야할듯?
'''
## 강사님꺼

# def cart(cur, start, total):
#     global result
#     if cur == n - 1:    # 모든 구역을 돌았을 경우
#         result = min(result, arr[start][0] + total)
#         return 
#     for i in range(1, n):
#         if visited[i] == 0 and start != i:
#             visited[i] = 1
#             cart(cur + 1, i, total + arr[start][i])
#             visited[i] = 0  # 방문표시 지우기

# T = int(input())
# for tc in range(1, T + 1):
#     n = int(input())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     visited = [0 for _ in range(n)]
#     result = float('INF')
#     cart(0, 0, 0)
#     print(f'#{tc} {result}')










## 내꺼

# def sun(i, N):
#     if i == N:
#         p.append(0)
#         p.insert(0,0)
#         result = 0
#         for k in range(len(p) - 1):
#             result += MAP[p[k]][p[k + 1]]
#         anslist.append(result)
#         p.pop()
#         p.pop(0)
#         return 
#     else:
#         for j in range(N):
#             if not used[j]:
#                 p[i] = j + 1
#                 used[j] = 1
#                 sun(i + 1, N)
#                 used[j] = 0

# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     MAP = [list(map(int,input().split())) for _ in range(N)]
#     used = [0] * (N - 1)
#     p = [0] * (N - 1)
#     anslist = []
#     sun(0, N - 1)
#     ans = min(anslist)
#     print(f'#{tc} {ans}')

    



# DP랑 비트로 풀기 <<- 확인해보기
T = int(input())  

for t in range(1, T+1):
    N = int(input())  
    arr = [list(map(int, input().split())) for _ in range(N)]

    dp = [[float('inf') for _ in range(1<<N)] for _ in range(N)]
    dp[0][1] = 0 

    for mask in range(1<<N):
        for cur in range(N):
            if dp[cur][mask] == float('inf'):  
                continue
            
            for nxt in range(N):
                if mask & (1<<nxt):  
                    continue
                next_mask = mask | (1<<nxt)
                dp[nxt][next_mask] = min(dp[nxt][next_mask], dp[cur][mask] + arr[cur][nxt])

    min_cost = min(dp[i][(1<<N) - 1] + arr[i][0] for i in range(1, N))

    print(f"#{t} {min_cost}")