# SWEA 노드의거리
'''
V개의 노드 개수와 방향성이 없는 E개의 간선 정보가 주어진다.
주어진 출발 노드에서 최소 몇 개의 간선을 지나면 
도착 노드에 갈 수 있는지 알아내는 프로그램을 만드시오.

[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄부터 테스트 케이스의 첫 줄에 V와 E가 주어진다. 5<=V=50, 4<=E<=1000
테스트케이스의 둘째 줄부터 E개의 줄에 걸쳐, 간선의 양쪽 노드 번호가 주어진다.
E개의 줄 이후에는 출발 노드 S와 도착 노드 G가 주어진다.

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
두 노드 S와 G가 서로 연결되어 있지 않다면, 0을 출력한다.


[input]
3
6 5
1 4
1 3
2 3
2 5
4 6
1 6
7 4
1 6
2 3
2 6
3 5
1 5
9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9

[output]
#1 2
#2 4
#3 3
'''


## 강사님 코드

# from collections import deque

# def BFS(start, end):
#     que = deque([(start, 0)])
#     while que:
#         n, cnt = que.popleft()
#         if not visited[n]:
#             visited[n] = 1
#         for j in arr[n]:
#             if not visited[j] and j == end:
#                 return cnt + 1
#             elif not visited[j]:
#                 que.append((j,cnt + 1))
#     return 0


# T = int(input())
# for tc in range(1,T + 1):
#     V, E = map(int,input().split())
#     arr = [[] for _ in range(V + 1)]
#     visited = [0] * (V + 1)
#     for i in range(E):      # 인접행렬
#         n1, n2 = map(int, input().split())
#         arr[n1].append(n2)
#         arr[n2].append(n1)
#     S, G = map(int,input().split())
#     print(f'#{tc} {BFS(S,G)}')


















# 내꺼(visited를 안쓰고 해봤음)

from collections import deque

def BFS(start, end):
    que = deque([(start, 0)])

    while que:
        a, level = que.popleft()
        if a == end:
            return level
        for i in range(1, V + 1):
            if adj[a][i] == 1:
                adj[a][i] , adj[i][a] = -1, -1 
                que.append((i, level + 1))
            
    else:
        return 0
            

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int,input().split()) # V는 노드 개수, E는 간선 개수
    arr = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int,input().split()) # S는 출발, G는 도착
    # 간선으로 주어졌으니까 인접행렬 만들어서 해보기
    adj = [[0 for _ in range(V + 1)] for _ in range(V + 1)]
    for e in arr:
        v1, v2 = e[0], e[1]
        adj[v1][v2], adj[v2][v1] = 1, 1     # 양방향

    print(f'#{tc} {BFS(S, G)}')
    
    
