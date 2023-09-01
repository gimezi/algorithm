# 최소환승
'''
민철이는 1번 지역에서 N번 지역에 있는 회사로 매일 출근합니다.
현재 직장을 오래 다녔던 민철이는 각 지역의 대중교통이
어떻게 연결되어 있는지 전부 알고 있기에 어느 상황에서든 최소로 환승하여 출근합니다.
어느날 T지역에 큰 화재가 발생하여 T번 지역으로 환승할 수 없게 되었습니다.
민철이는 T번 지역을 피해 회사로 최대한 환승을 적게 하여 출근하고자 할 때,
그 최소 환승 횟수를 출력하는 프로그램을 작성해 주세요.


입력

첫 번째 줄에 지역의 수 N과 대중교통으로이동 가능한 관계의 수 
M이 공백을 구분으로 주어집니다.(1 ≤ N ≤ 10 , 0≤ M≤ 45)
두 번째 줄부터 M개의 줄에 걸쳐에 정수 A, B가 공백을 구분으로 
주어지며 A와 B는서로 간에대중교통으로 1번의 환승으로 갈 수 있다는 것을 의미합니다. (1≤ A,B≤ N)
단, A와 B가 같은 경우는 존재하지 않습니다.
마지막 줄에 화재가 발생한 지역 T가 주어집니다.(1 <T )

출력

T번 지역을 피해 N번 지역으로 출근할 수 있는 최소 환승을 출력합니다.
단, 출근할 수 있는 방법이 없다면 -1을 출력합니다.


[input]
8 11
1 2 
1 3
1 5
1 7
2 7
2 4
4 7
4 6
6 8
8 7
5 3
7

[output]
4

'''
from collections import deque

N, M = map(int,input().split())
arr = [[] for _ in range(N + 1)]
for _ in range(M):
    n1, n2 = map(int,input().split())
    arr[n1].append(n2)
    arr[n2].append(n1)
T = int(input())
arr[T] = []
for i in arr:       # 불난 곳 지워버리기
    if T in i:
        i.remove(T)
# 시작은 1번부터, 도착은 N번까지

def BFS(start, end):
    que = deque([start])
    visited = [0 for _ in range(N + 1)]
    visited[start] = 1

    while que:
        now = que.popleft()
        if now == end:
            return visited[now] -1 
        for i in range(1, N + 1):
            if not visited[i] and i in arr[now]:
                visited[i] = visited[now] + 1
                que.append(i)
    return -1

print(BFS(1, N))