# 출근하기 편한 지역 (SWEA)

'''
N개의 지역에 대한 버스 노선도의 정보가 주어질 때,
민철이가 편하게 출근할 수 있는 지역의 후보지가 몇 군데있는지 출력하는 프로그램을 작성해 주세요.

입력
첫 번째 줄에 지역의 수 N과 버스로 이동 가능한 관계의 수 M이 
공백을 구분으로 주어집니다.(1 ≤ N≤ 10 , 0≤ M≤ 45)
지역의 번호는 1부터 N까지의 번호가 부여됩니다.
두 번째 줄부터 M개의 줄에 걸쳐정수A, B가 공백으로 구분되어 주어집니다.
A와 B는 한 버스의 이동 경로를 의미하며, 
A에서 B 방향으로, 또는 B에서 A방향으로 이동할 수 있습니다. (1≤ A, B≤ N,A =/= B)
마지막 줄에직장이 존재하는 지역 R과출근하기 편하다는기준이 되는 
버스 탑승 횟수 K가 공백으로 구분되어 주어집니다.(1 ≤ R≤ N , 0≤ K≤9)


[input]
10 9
1 2
7 1
6 7
3 7
5 4
10 9
9 8
3 8
4 3
1 3

[output]
7

'''
from collections import deque

N, M = map(int, input().split())
arr = [[] for _ in range(N + 1)]
for _ in range(M):
    n1, n2 = map(int,input().split())
    arr[n1].append(n2)
    arr[n2].append(n1)

start, limit = map(int, input().split())    # 집 위치랑, 한계
cnt = 0

def BFS(start, end):
    global cnt
    visited = [0 for _ in range(N + 1)]
    que = deque([(start, 0)])
    visited[start] = 1
    while que:
        now, level = que.popleft()
        # print(visited)
        if now == end:
            if level <= limit:
                cnt += 1
                return
            else: return
        for i in range(N + 1):
            if i in arr[now] and visited[i] == 0:
                visited[i] = 1 
                que.append((i, level + 1))
    return 

for i in range(1, N + 1):
   
    BFS(start, i)

print(cnt)
        