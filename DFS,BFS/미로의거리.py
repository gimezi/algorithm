# swea 미로의거리
'''
NxN 크기의 미로에서 출발지 목적지가 주어진다.
이때 최소 몇 개의 칸을 지나면 출발지에서 도착지에 다다를 수 있는지 알아내는 프로그램을 작성하시오.
경로가 있는 경우 출발에서 도착까지 가는데 지나야 하는 최소한의 칸 수를,
경로가 없는 경우 0을 출력한다.
다음은 5x5 미로의 예이다. 1은 벽, 0은 통로를 나타내며 미로 밖으로 벗어나서는 안된다.

13101
10101
10101
10101
10021

마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 
맨 윗줄의 3에 5개의 칸을 지나 도착할 수 있다.


[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 
미로의 통로와 벽에 대한 정보가 주어진다. 5<=N<=100
0은 통로, 1은 벽, 2는 출발, 3은 도착이다.

3
5
13101
10101
10101
10101
10021
5
10031
10111
10101
10101
12001
5
00013
01110
21000
01111
00000

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

#1 5
#2 5
#3 0

'''

# DFS로 풀어보기

def DFS(y, x):
    stack = [(y, x)]
    visited = [[0 for col in range(N)]for row in range(N)]
    visited[y][x] = 1
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while stack:
        cy, cx = stack[-1]
        for dy, dx in direction:
            ny = cy + dy
            nx = cx + dx
            if 0 <= ny < N and 0 <= nx < N:
                # print(ny,nx)
                # print(visited)
                if arr[ny][nx] == 0 and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    stack.append((ny, nx))
                    # print(stack)
                    break
                if arr[ny][nx] == 3:
                    result = len(stack) - 1
                    return result
        else:
            if stack:
                stack.pop()
    
    return 0




# BFS로도 풀어보기

from collections import deque

def BFS(y, x):
    que = deque([(y, x)])
    visited = [[0 for col in range(N)]for row in range(N)]
    visited[y][x] = 1
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while que:
        cy, cx = que.popleft()    
        for dy, dx in direction:
            ny = cy + dy
            nx = cx + dx
            if 0 <= ny < N and 0 <= nx < N:
                if arr[ny][nx] == 0 and visited[ny][nx] == 0:
                    que.append((ny,nx))
                    visited[ny][nx] = visited[cy][cx] + 1
                elif arr[ny][nx] == 3:
                    return visited[cy][cx] - 1
                
    return 0


## 출력용

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 2:
                ay = y
                ax = x
    # print(ay, ax)
    print(f'#{tc} {BFS(ay, ax)}')
    
    
    

## 강사님 코드

def pro_bfs(y, x):
    que = []
    que.append((y, x))
    visited[y][x] = 1
    while que:
        cy, cs = que.pop(0)
        if arr[cy][cx] == '3':
            return visited[cy][cs] - 2      # 시작과 끝 제외
        for dy, dx in direction:
            ny, nx = cy + dy, cs + dx
            if 0 <= ny < N and 0 <= nx < N:
                if arr[ny][nx] != 1 and visited[ny][nx] == 0:
                    visited[ny][nx] = visitied[cy][cs] + 1
                    que.append((ny, nx))

    return 0









                