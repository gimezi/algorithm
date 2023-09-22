# Union - Find?
def find(x):
    if x == parent[x]:
        return x
    else:
        return find(parent[x])

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int,input().split())
    parent = [i for i in range(N + 1)]
    arr = [list(map(int,input().split())) for _ in range(M)]
    for a, b in arr:
        parent[find(a)] = find(b)

    ans = 0
    for i in range(1, N + 1):
        if i == parent[i]:
            ans += 1
    print(f'#{tc} {ans}')



    # group = []
    # for i in range(1, N + 1):
    #     if parent[i] in group:
    #         continue
    #     else:
    #         group.append(parent[i])
    # print(f'#{tc} {len(group)}')
    