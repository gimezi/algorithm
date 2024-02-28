# 중위순회
'''
[input]

8
1 W 2 3
2 F 4 5
3 R 6 7
4 O 8
5 T
6 A
7 E
8 S

[output]
#1 SOFTWARE
'''

def inorder(p, N): # N: 완전이진트리의 마지막 정점
    if p <= N:
        inorder(p * 2, N)          # 왼쪽 자식으로 이동
        print(tree[p], end ='')    # 중위순회에서 할 일
        inorder(p * 2 + 1, N)      # 오른쪽 자식으로 이동
        

T = 10
for tc in range(1, T + 1):
    N  = int(input())
    tree = [0] * (N + 1)    # N번 노드까지 있는 완전이진트리
    for _ in range(N):
        arr = list(input().split())
        tree[int(arr[0])] = arr[1]

    # 중위순회
    print(f'#{tc}', end = ' ')
    inorder(1, N)           # root = 1
    print()


















# import math

# N = int(input())
# arr = [0 for _ in range(N + 1)]
# for _ in range(N):
#     node = list(input().split())
#     if len(node) == 2:
#         num = int(node[0])
#         arr[num] = node[1]
#     else:
#         num = int(node[0])
#         arr[num] = [node[1],list(map(int,node[2:]))]

# a = int(math.log2(N))
# start = 2 ** a
# visited = [0 for _ in range(N + 1)]
# result = []
# # [0, ['W', [2, 3]], ['F', [4, 5]], ['R', [6, 7]], ['O', [8]], 'T', 'A', 'E', 'S']

# def find(start):
#     print(visited, start)
#     if sum(visited) == N:
#         return result
#     if visited[start] == 0 and arr[start] and len(arr[start]) == 1:
#         visited[start] = 1
#         result.append(arr[start][0])
#         print(arr[start])
#         start = start // 2
#         find(start)
#     elif arr[start]:
#         for num in arr[start][1]:
#             print(num)
#             if visited[num] == 0:
#                 visited[num] = 1
#                 find(num)
#                 print(arr[start])
#             else:
#                 start = start // 2
#                 find(start)
            

# find(start)

# # 안댕
