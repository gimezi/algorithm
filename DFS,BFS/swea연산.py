from collections import deque

def find(n, m):
    que = deque([(n, 0)])
    visited = [0] * 1000001
    visited[n] = 1
    while que:
        now, level = que.popleft()
        if now == m:
            return level
        for nextnum in [now+1, now -1, now * 2, now - 10]:
            if 0 < nextnum <= 1000000:
                if visited[nextnum] == 0:
                    visited[nextnum] = 1
                    que.append((nextnum, level + 1))

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int,input().split())
    ans = find(N, M)
    print(f'#{tc} {ans}')
