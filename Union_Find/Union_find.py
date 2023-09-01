# Union Find
'''
첫 번째 줄에 N과 Query의 개수 Q가 입력됩니다. (1 <= N, Q <= 1,000)
두 번째 줄부터 [K, A, B] 형태로 입력이 주어집니다. (1 <= A, B <= N, A ≠ B)

[0, A, B] : 노드 A, B가 서로 같은 그룹 이라면 YES, 아니면 NO 를 출력합니다. 
[1, A, B] : 노드 A, B를 연결합니다.


[입력]
4 5
1 1 2
1 3 4
0 2 4
1 2 4
0 1 2

[출력]
NO
YES
'''

def find(node):
    if node != root(node):
        root[node] = find(root[node])
    return root[node]

def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if rank[root_x] > rank[root_y]:
        root[root_y] = root_x
    else:
        root[root_x] = root_y
        if rank[root_x] == root_y:
            rank[root_y] += 1

N, Q = map(int,input().split())
rank = [0] * (N  + 1)
root = [i for i in range(N + 1)]
for _ in range(Q):
    K, A, B = map(int,input().split())
    if K == 0:
        if find(A) == find(B):
            print('YES')
        else:
            print('NO')
    else:
        union(A, B)
        
















# def find(a, b):
#     que = [a]
#     visited = [0 for _ in range(N + 1)]
#     visited[a] = 1

#     while que:
#         now = que.pop(0)
#         if now == b:
#             return 'YES'
#         for i in range(N + 1):
#             if adj[now][i] == 1 and visited[i] == 0:
#                 que.append(i)
#                 visited[i] = 1               
#     return 'NO'


# N, Q = map(int,input().split())
# adj = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
# for _ in range(Q):
#     fun, a, b = map(int,input().split())
#     if fun:
#         adj[a][b] = 1
#         adj[b][a] = 1
#     else:
#         print(find(a, b))