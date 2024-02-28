# # Union - Find?
# def find(x):
#     if x == parent[x]:
#         return x
#     else:
#         return find(parent[x])

# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int,input().split())
#     parent = [i for i in range(N + 1)]
#     arr = [list(map(int,input().split())) for _ in range(M)]
#     for a, b in arr:
#         parent[find(a)] = find(b)

#     ans = 0
#     for i in range(1, N + 1):
#         if i == parent[i]:
#             ans += 1
#     print(f'#{tc} {ans}')



    # group = []
    # for i in range(1, N + 1):
    #     if parent[i] in group:
    #         continue
    #     else:
    #         group.append(parent[i])
    # print(f'#{tc} {len(group)}')
    
# DFS로 해보고 싶어요


def DFS(start):
    global cnt
    stack = [start]
    while stack:
        now = stack.pop()
        for next_people in arr[now]:    # 지금 사람의 친구들 중
            if visited[next_people] == 0:   # 안들린 사람이라면
                visited[next_people] = 1    # 방문처리
                stack.append(next_people)
    cnt += 1     # 함수 다 돌렸다면 그룹갯수 +1

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int,input().split())
    arr = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int,input().split())
        arr[a].append(b)    
        arr[b].append(a)    # 양방향
    visited = [0 for _ in range(N + 1)]
    cnt = 0     # 그룹의 갯수
    for i in range(1, N + 1):
        if visited[i] == 0:     # 확인 안한 사람만 dfs를 돌려줌
            DFS(i)
    print(f'#{tc} {cnt}')

    