# SWEA 배열 최소 합

'''
NxN 배열에 숫자가 들어있다. 
한 줄에서 하나씩 N개의 숫자를 골라 합이 최소가 되도록 하려고 한다. 
단, 세로로 같은 줄에서 두 개 이상의 숫자를 고를 수 없다.

조건에 맞게 숫자를 골랐을 때의 최소 합을 출력하는 프로그램을 만드시오.

[input]
3
3
2 1 2
5 8 5
7 2 2
3
9 4 7
8 6 5
5 3 7
5
5 2 1 1 9
3 3 8 3 1
9 2 8 8 6
1 5 7 8 3
5 5 4 6 8

'''


# 강사님 코드


def DFS(idx, now_sum):
    global min_sum
    if now_sum >= min_sum:
        return
    if idx == N:
        if min_sum > now_sum:
            min_sum = now_sum
            return
    for i in range(N):
        if not used[i]:
            used[i] = 1
            DFS(idx + 1, now_sum + arr[idx][i])
            used[i] = 0
        
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * (N + 1)
    min_sum = 28e10

    DFS(0,0)
    print(f'#{tc} {min_sum}')





# def back_tracking(level, total):
#     global min_v
#     if level == N:
#         if min_v > total:  # 계산한 값이 기존의 최솟값보다 작으면 갱신
#             min_v = total
#             return
#     elif total >= min_v:  # 중간까지 계산한 값이 이미 최솟값과 같거나 큰 경우
#         return
#     else:
#         for j in range(level, N):
#             A[level], A[j] = A[j], A[level]
#             back_tracking(level + 1, total+arr[level][A[level]-1])
#             A[level], A[j] = A[j], A[level]

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     min_v = (9*N)+1
#     arr = [list(map(int, input().split()))for _ in range(N)]
#     A = [i for i in range(1, N+1)]
#     back_tracking(0, 0)
#     print(f'#{tc} {min_v}')









# def DFS(level, sum):
#     global minval,path
#     if level == N:
#         if sum < minval:
#             minval = sum
#         return
    
#     for i in range(level, N):
        
       
            

# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     lst = [list(map(int, input().split())) for _ in range(N)]
#     minval = 21e8
#     DFS(0,0)
#     print(f'#{tc} {minval}')


    
    





























# # 순열구해서 하는 방법
# T = int(input())

# def f(i, N, ans, P):
#     global minval
#     print(ans)
#     if i == N and ans < minval:
#         minval = ans
#         return
    
#     if ans > minval:
#         return
    
#     else:
#         for j in range(N):
#             if j not in P:
#                 P[i] = j
#                 print(P)
#                 f(i + 1, N, ans + arr[i][j], P)
#                 P[i] = -1
                
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int,input().split())) for _ in range(N)]
#     A = [-1] * N
#     minval = 10000
#     f(0, N, 0, A)
#     print(f'#{tc} {minval}')



# 처음에 낸거
# T = int(input())

# def f(i, N, ans, P):
#         global minval
#         if i == N and ans < minval:
#              minval = ans
#         elif ans > minval:
#              return
            
#         else:
#             for j in range(i, N):           # 자신부터 오른쪽 끝까지
#                 A[i], A[j] = A[j], A[i]
#                 f(i+1, N, ans + arr[i][j], A)
#                 A[i], A[j] = A[j], A[i]     # 원상복구


# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int,input().split())) for _ in range(N)]
#     A = list(range(N))
#     minval = 10000
#     f(0, N, 0, A)  
#     print(f'#{tc} {minval}')



## 내꺼아님

# def subsum(r, s, N, p):
#     global res
#     if r == N and s < res:
#         res = s
#         return

#     if s > res:
#         return

#     else:
#         for c in range(N):
#             if c not in p:
#                 p[r] = c
#                 subsum(r + 1, s + arr[r][c], N, p)
#                 p[r] = -1


# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     p = [-1] * (N*1)
#     res = 1000000
#     subsum(0, 0, N, p)
#     print(f'#{tc} {res}')