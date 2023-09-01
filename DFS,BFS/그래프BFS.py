# SWEA 그래프 BFS

'''
아래에 그래프가 놓여져 있습니다.
입력 받은 출발 지점에서 너비 우선 탐색법으로 그래프를 탐색해주세요.
한번 방문했던 노드는 다시 방문할 수 없습니다.
시작 지점부터 BFS가 끝날때까지 방문한 노드를 출력해주세요.
'''
from collections import deque

adj = [
    [0, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1],
    [0, 0, 1, 1, 0, 0]
]

N = int(input())
visited = [0] * 6


def BFS(start):
    que = deque([start])
    visited[start] = 1
    anslst = []
    while que:
        a = que.popleft()
        anslst.append(a)
        for i in range(6):
            if adj[a][i] == 1 and visited[i] == 0:
                que.append(i)
                visited[i] = 1
        
    return anslst

for i in BFS(N):
    print(i)

