from collections import deque

start = int(input())
end = int(input())


def DFS(start, end):
    que = deque([start])
    visited = [0 for _ in range(100001)]

    while que:
        now = que.popleft()
        if now == end:
            return visited[now] 
        for i in (now // 2, now * 2, now + 1, now - 1):
            try:
                if not visited[i] and 0 <= i <= 100000:
                    visited[i] = visited[now] + 1
                    que.append(i)
            except:
                continue
        
print(DFS(start, end))

