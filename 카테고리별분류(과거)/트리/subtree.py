# subtree - tree 기본

# T = int(input())
# for tc in range(1, T + 1):

#     E, N =  map(int,input().split())
#     arr = list(map(int, input().split()))

#     c = [[0 for _ in range(E + 2)] for _ in range(2)]

#     for i in range(E):
#         parent = arr[2 * i]
#         child = arr[2 * i + 1]
#         if c[0][parent]:
#             c[1][parent] = child
#         else:
#             c[0][parent] = child
#     cnt = 0

#     def preorder(n):
#         global cnt
#         if n:
#             cnt += 1 
#             print(n)
#             preorder(c[0][n])  # 왼쪽 서브트리로 이동
#             preorder(c[1][n])
            
            
#     preorder(N)
#     print(f'#{tc} {cnt}')



# 강사님 코드
def sub_tree(node):
    global cnt
    for i in range(2):          # 왼쪽자식, 오른쪽자식
        if tree[i][node]:       # 해당 노드의 자식이 있다면
            cnt += 1
            n = tree[i][node]   # 자식 노드의 번호
            sub_tree(n)         # 자식 노드에 대해 재귀호출
    
T = int(input())
for tc in range(1, T + 1):
    E, N = map(int,input().split())
    temp = input().split()
    tree = [[0 for _ in range(E + 2)] for _  in range(2)]
    for i in range(E):
        p_node = int(temp[2 * i])
        c_node = int(temp[2 * i + 1])
        if tree[0][p_node] == 0:
            tree[0][p_node] = c_node
        else:
            tree[1][p_node] = c_node
    cnt = 1
    sub_tree(N)
    print(f'#{tc} {cnt}')