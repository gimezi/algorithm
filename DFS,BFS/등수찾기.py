# 등수 찾기

# 전체 학생수, 질문 수, 타겟
n, m, target = map(int,input().split())

upv = [[] for _ in range(n + 1)]
downv = [[] for _ in range(n + 1)]

# up: target보다 못한 학생 수, down: target보다 잘한 학생 수
up = 1
down = 1

upused = [False] * (n + 1)
downused = [False] * (n + 1)

# target보다 못한 학생들을 탐색하는 DFS함수
def updfs(node):
    global up
    for next_node in upv[node]:
        if not upused[next_node]:
            up += 1
            upused[next_node] = True
            updfs(next_node)

def downdfs(node):
    global down
    for next_node in downv[node]:
        if not downused[next_node]:
            down += 1
            downused[next_node] = True
            downdfs(next_node)

for _ in range(m):
    a, b = map(int,input().split())
    upv[b].append(a)
    downv[a].append(b)

updfs(target)
downdfs(target)
print(up)   # 가장 높은 점수
print(n - down + 1)     # 가장 낮은 점수


















# N, M, X = map(int,input().split())
# parent = [0 for _ in range(N + 1)]
# arr = [[] for _ in range(N + 1)]
# for _ in range(M):
#     a, b = map(int,input().split())
#     parent[b] = a
#     arr[b].append(a)

# for i in range(N + 1):
#     if parent[i] == 0 and i in parent:
#         grandma = i     # 제일 위에 있는애부터 찾아주기
# print(grandma)