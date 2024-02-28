# SWEA 다빈치민코드

'''
N개의 숫자들 중, M개의 숫자를 골라서 곱했을 때
최소가 되는 조합을 구하세요

[input]
7 3
1 5 4 -2 6 7 -1

[output]
-2 6 7
'''

## DFS랑 백트래킹을 써서 풀어야한다네

import copy

N, M = map(int,input().split())
lst = list(map(int, input().split()))
path = []
visited = [0] * N
minval = 21e8
result = []

def DFS(level, sum):
    global minval, path, result
    if level == M:              # 패를 모두 선택했다면
        if sum < minval:        # 현재 곱한 값이 최소값인지?
            minval = sum
            result = copy.deepcopy(path)
        return
    
    for i in range(N):
        if visited[i] == 1:     # 이미 사용한거면 건너뜀
            continue
        path.append(lst[i])
        visited[i] = 1
        DFS(level + 1, sum * lst[i])
        visited[i] = 0          # 복구(백트래킹)
        path.pop()

DFS(0, 1)
result.sort()
print(*result)









# def find_subset():
#     global minval
#     lst =[]
#     for i in range(1 << N):
#         sub = []
#         for j in range(N):
#             if i & (1 << j):
#                 sub.append(arr[j])
#                 if len(sub) == M:
#                     break
#         lst.append(sub)
    
#     stack = []
#     for l in lst:
#         if len(l) == M:
#             mult = 1
#             for k in range(M):
#                 mult *= l[k]
#             if mult < minval:
#                 minval = mult
#                 stack.append(l)

#     return stack[-1]
        
        
# N, M = map(int,input().split())
# arr = list(map(int,input().split()))
# minval = 100000000000
# A = [10000] * M
# find_subset().sort()
# print(*find_subset())