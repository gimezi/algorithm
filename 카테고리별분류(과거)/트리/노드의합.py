# 노드의 합

# 내꺼
# T = int(input())
# for tc in range(1, T + 1):
#     N, M, L = map(int,input().split())
#     tree = [0 for _ in range(3 * N)]
#     for _ in range(M):
#         a, b = map(int,input().split())
#         tree[a] = b
#     # print(tree)
    
#     while N >= 1:
#         if not tree[N]:
#             tree[N] = tree[2 * N] + tree[2 * N + 1]
#         N -= 1

#     print(f'#{tc} {tree[L]}')


T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int,input().split())
    tree = [0 for _ in range(N + 1)]
    for i in range(M):
        idx, value = map(int,input().split())
        tree[idx] = value
    for i in range(N, 0, -1): # 역순
        if i // 2 > 0:
            tree[i // 2] += tree[i]
    result = tree[L]
    print(f'#{tc} {result}')
