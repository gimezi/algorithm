# 다시해보기



tree = [[-1, -1] for _ in range(1001)]
N = 0
preorder = []
inorder = []
postorder = []

def dfs(now):
    if now == -1:
        return
    preorder.append(now)
    dfs(tree[now][0])
    inorder.append(now)
    dfs(tree[now][1])
    postorder.append(now)


N = int(input())
for _ in range(N):
    root, left, right = map(int,input().split())
    tree[root][0] = left
    tree[root][1] = right
dfs(1)
print(' '.join(map(str, inorder)))
print(' '.join(map(str, preorder)))
print(' '.join(map(str, postorder)))