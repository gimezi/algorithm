# 백준 미네랄
'''
5 6
......
..xx..
..x...
..xx..
.xxxx.
1
3


12 24
........................
........................
..........xxxxxxxxxxx...
..........x.........x...
..........x.........x...
..........x.........x...
..........x.........x...
..........xxxxxxxxxxx...
..............x.........
..............x.........
..............x.........
..............x.........
1
10

마ㅏ자따ㅏㅏㅏ

'''
from collections import deque

# y, x는 현재 뿌셔진 위치
def BFS(y, x):
  q = deque([(y, x)])
  ans = [(y, x)]
  visited = [[0 for _ in range(C)] for _ in range(R)]
  visited[y][x] = 1
  while q:
    nowy, nowx = q.popleft()
    # 이어진게 바닥까지 가면
    if nowy == R - 1:
      return False
    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
      nexty, nextx = nowy + dy, nowx + dx
      if 0 <= nexty < R and 0 <= nextx < C:
        if visited[nexty][nextx] == 0:
          # 방문표시는 다 해주고,
          visited[nexty][nextx] = 1
          # 벽이라면, 
          if cave[nexty][nextx] == 'x':
            # 이어진 블록에도 넣고 / 큐에도 넣고
            ans.append((nexty, nextx))
            q.append((nexty, nextx))
  return ans


# 상하좌우에 블럭 체크 해주는 함수
def Check(y,x):
  for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
    ny, nx = y + dy, x + dx
    if 0 <= ny < R and 0 <= nx < C:
      # 그 위치에서 BFS돌려주기
      if cave[ny][nx] == 'x':
        temp = BFS(ny, nx)
        if temp:
          return temp
  return False
    
R, C = map(int,input().split())
cave = []
for _ in range(R):
  cave.append(list(input()))
N = int(input())
heights = list(map(int,input().split()))

for i in range(N):
  # 이번에 부셔졌는지
  isBreak = False
  # 홀수 번 째(오른쪽)
  if i % 2:
    for j in range(C - 1, -1, -1):
      # 오른쪽으로부터 처음으로 만나는 x라면,
      if cave[R - heights[i]][j] == 'x':
        # 부셔진걸 알려주고
        isBreak = True
        # 어디가 부셔진지 알려주기
        crack = (R - heights[i], j)
        # 뿌셨으니까 없애주기
        cave[R - heights[i]][j] = '.'
        break
  # 짝수번 째(왼쪽)
  else:
    for j in range(C):
      # 왼쪽으로부터 처음으로 만나는 x라면,
      if cave[R - heights[i]][j] == 'x':
        # 부셔진걸 알려주고
        isBreak = True
        # 어디가 부셔진지 알려주기
        crack = (R - heights[i], j)
        # 뿌셨으니까 없애주기
        cave[R - heights[i]][j] = '.'
        break
  
  # 만약에 블록이 이번에 부셔졌다면,
  if isBreak:
    temp = Check(crack[0], crack[1])
    # 떨어질게 있다면
    if temp:
      for y, x in temp:
        cave[y][x] = '.'

      while True:
        for a, b in temp:
          if a + 1 == R:
            break
          if 0 <= a + 1 < R and cave[a + 1][b] == 'x':
            break
          
        else:
         temp = [(x + 1, y) for x, y in temp]
         continue
        break

      for y, x in temp:
        cave[y][x] = 'x'

for l in range(R):
  print(''.join(cave[l]))
