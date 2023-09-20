# 코딩 던전

from collections import deque

N, M, K = map(int,input().split())
MAP = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, g = map(int,input().split())
    MAP[a].append((b,g))


def gogo(start):
    que = deque([(start, 0)])
    visited = [0 for _ in range(N + 1)]
    visited[start] = 1
    able = []
    while que:
        now, gold = que.popleft()
        if gold <= K:
            able.append(now)
        for n, g in MAP[now]:
            if visited[n] == 0:
                que.append((n, gold + g))
    return able

result = gogo(0)
result.sort()
result.pop(0)
print(*result)