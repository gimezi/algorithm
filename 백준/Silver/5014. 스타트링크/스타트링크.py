# 스타트링크(백준)
'''
총 f층
s에 있고
g로 가야함
u만큼 위로
d만큼 밑으로 갑니다.

BFS
'''
from collections import deque

f, s, g, u, d = map(int,input().split())

def BFS():
  q = deque([(s, 0)])  # 현재 위치, step
  visited = [0 for _ in range(f + 1)]
  visited[s] = 1
  while q:
    now, step = q.popleft()
    if now == g:
      return step
    for dx in [u, -1 * d]:
      next = now + dx
      if 0 < next <= f:
        if visited[next] == 0:
          visited[next] = 1
          q.append((next, step + 1))
  return 'use the stairs'

print(BFS())