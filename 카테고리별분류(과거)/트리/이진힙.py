# 이진 힙
'''
3
6
7 2 5 3 4 6
6
3 1 4 16 23 12
8
18 57 11 52 14 45 63 40

#1 7
#2 5
#3 65
'''

# def BST(node, n):   # 노드랑 순서
#     if n <= N:
#         tree[n] = node
#         while n > 1 and tree[n] < tree[n // 2]:
#             tree[n], tree[n // 2] = tree[n // 2], tree[n]
#             n //= 2


# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = list(map(int,input().split()))
#     tree = [0 for _ in range(N + 1)]
#     for i in range(N):
#         BST(arr[i], i + 1)
#     # print(tree)
#     result = 0
#     while N > 0:
#         result += tree[N//2]
#         N = N // 2
#     print(f'#{tc} {result}')


# heapq라이브러리를 이용한 풀이
import heapq
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    tree = []
    number = map(int,input().split())
    for num in number:
        heapq.heappush(tree, num)
    sum_v = 0
    N = len(tree) // 2
    while N:
        sum_v += tree[N - 1]
        N //= 2
    print(sum_v)
