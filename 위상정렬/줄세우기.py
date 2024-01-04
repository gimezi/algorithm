# 줄 세우기
'''
백준
위상 정렬

- 진입차수(Indegree): 특정한 노드로 들어오는 간선의 개수
- 진출차수(Outdegree): 특정한 노드에서 나가는 간선의 개수
'''
from collections import deque

N, M = map(int,input().split())

# 진입차수
indegree = [0 for _ in range(N + 1)]
# 각 학생 별로 compare[2] = [1, 4]라면 2보다 1, 4가 더 크다는걸 나타내기 위한 리스트
compare = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int,input().split()) # a가 b보다 먼저
    indegree[b] += 1
    compare[a].append(b)

result = [] # 결과 리스트
q = deque() # 위상 정렬은 큐를 이용하여 구현

# 진입차수가 0인 애부터 q에 넣어주기
for i in range(1, N + 1):
    if not indegree[i]:
        q.append(i)

# 큐가 빌 때까지 반복하면서
while q:
    now = q.popleft()
    result.append(now)
    for next in compare[now]:
        indegree[next] -= 1
        if indegree[next] == 0:
            q.append(next)

print(*result)
