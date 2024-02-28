# 15649번 N과 M(1)

'''
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을
모두 구하는 프로그램을 작성하시오.
1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

[입력]
첫줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)'

[출력]
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다.
중복되는 순열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
수열은 사전 순으로 증가하는 순서로 출력해야 한다.

3 1


1
2
3
'''


# N과 M (2)

N, M = map(int,input().split())
arr = []

def make(arr):
    if len(arr) == M:
        for i in range(M - 1):
            if arr[i] >= arr[i + 1]:
                return
        print(*arr)
        return
    for i in range(1, N + 1):
        if i not in arr:
            arr.append(i)
            make(arr)
            arr.pop()   # 백트래킹
make(arr)



# N과 M (1)
N, M = map(int,input().split())
arr = []

def make(arr):
    if len(arr) == M:
        print(*arr)
        return
    for i in range(1, N + 1):
        if i not in arr:
            arr.append(i)
            make(arr)
            arr.pop()   # 백트래킹
make(arr)


























# N, M = map(int,input().split())

# def find(num, m):   # n이 시작하는 번호(맨 앞 번호), m은 갯수
#     stack = [num]
#     while stack:
#         now = stack.pop()
#         if len(ans) == m:
#             print(ans)
#             find(num, m)  
#         for i in range(1, m + 1):
#             if not visited[i] and i != now:
#                 ans.append(now)
#                 visited[i] = 1
#                 stack.append(i)

# for i in range(1, N + 1):
#     visited = [0 for _ in range(N + 1)]
#     visited[i] = 1
#     ans = []
#     result = find(i, M)     
