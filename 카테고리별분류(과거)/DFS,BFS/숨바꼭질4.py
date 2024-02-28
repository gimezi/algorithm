# 숨바꼭질4
'''
+1, -1, *2의 위치로 이동
이동할 때마다 1초
가장 빠른길, 그때의 경로도 같이
'''
from collections import deque

N, M = map(int,input().split())
def find(start, end):
    que = deque([(start, 0, str(start) + ' ')])
    visited = [0 for _ in range(100001)]
    visited[start] = 1
    while que:
        now, level, path = que.popleft()
        if now == end:
            return level, path
        for next in [now * 2, now - 1, now + 1]:
            if 0 <= next < 100001:
                if visited[next] == 0:
                    visited[next] = 1
                    que.append((next, level + 1, path + str(next) + ' '))

t, path = find(N, M)
print(t)
path = list(map(int, path.split()))
print(*path)