# 트리인접행렬 BFS
'''
트리 자료구조에서 너비 우선 탐색법으로 각 노드를 탐색해주세요.
시작 지점 부터, 노드에 방문할 때마다 값을 출력 해주세요.
출발지점은 입력으로 주어 집니다.
한번 방문 했던 노드는 방문할 수 없습니다.
트리 자료구조는 인접행렬로 하드코딩 해주세요.
'''

from collections import deque

adj = [
    [0, 1, 0, 0, 1, 0], 
    [0, 0, 1, 0, 0, 1], 
    [0, 0, 0, 1, 0, 0], 
    [0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0]
    ]



N = int(input())       # 시작점

def BFS(start):
    que = deque([start])
    visited = [0] * 6
    visited[start] = 1
    anslst = []
    

    while que:
        a = que.popleft()
        anslst.append(a)
        for i in range(6):
            if adj[a][i] == 1 and visited[i] == 0:
                visited[i] = 1
                que.append(i)
    return anslst

print(*BFS(N))
            

