# 두번째로 DP로 풀어보자

# 테케 번호
k = 1
while True:
  l = int(input())
  # 0이면 입력 끝
  if l == 0:
    break
  arr = []
  for _ in range(l):
    arr.append(list(map(int,input().split())))
  
  DP = [[float('inf') for _ in range(3)] for _ in range(l)]
  # 첫번째 행은 채워넣어주자
  DP[0] = [float('inf'), arr[0][1], arr[0][1] + arr[0][2]]
  for i in range(1, l):
    DP[i][0] = min(DP[i - 1][0], DP[i - 1][1]) + arr[i][0]
    DP[i][1] = min(DP[i - 1][0], DP[i -1][1], DP[i -1][2], DP[i][0]) + arr[i][1]
    DP[i][2] = min(DP[i -1][1], DP[i -1][2], DP[i][1]) + arr[i][2]

  print(f'{k}.', DP[l - 1][1])
  k += 1


# 첫번째 다익스트라로 풀었더니 메모리 초과가 남

# import heapq

# # 갈 수 있는 곳 -> 밑으로만 감, 대각선으로 가능
# dire = [(0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

# def find(arr, n):
#   visited = [[float('inf') for _ in range(3)] for _ in range(n)]
#   visited[0][1] = arr[0][1]
#   pq = []
#   heapq.heappush(pq, (arr[0][1], (0, 1)))

#   while pq:
#     cost, now = heapq.heappop(pq)
#     if cost <= visited[now[0]][now[1]]:
#       for dy, dx in dire:
#         ny, nx = now[0] + dy, now[1] + dx
#         if 0 <= ny < n and 0 <= nx < 3:
#           if arr[ny][nx] + cost < visited[ny][nx]: 
#             visited[ny][nx] = arr[ny][nx] + cost
#             heapq.heappush(pq, (arr[ny][nx] + cost, (ny, nx)))
  
#   return visited[n-1][1]

# # 테케 번호
# k = 1
# while True:
#   l = int(input())
#   # 0이면 입력 끝
#   if l == 0:
#     break
#   arr = []
#   for _ in range(l):
#     arr.append(list(map(int,input().split())))
#   print(f'{k}.', find(arr, l))
#   k += 1
