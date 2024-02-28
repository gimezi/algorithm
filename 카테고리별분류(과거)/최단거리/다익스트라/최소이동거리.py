# 최소이동거리
# 다익스트라
'''
A도시에는 E개의 일방통행 도로 구간이 있으며, 
각 구간이 만나는 연결지점에는 0부터 N번까지의 번호가 붙어있다.

구간의 시작과 끝의 연결 지점 번호, 구간의 길이가 주어질 때, 
0번 지점에서 N번 지점까지 이동하는데 
걸리는 최소한의 거리가 얼마인지 출력하는 프로그램을 만드시오.
모든 연결 지점을 거쳐가야 하는 것은 아니다.



누적거리가 최소가 되도록?
'''

import heapq

T = int(input())
for tc in range(1, T + 1):
    N, E = map(int,input().split())
    nodes = [[] for _ in range(N + 1)]
    for _ in range(E):
        s, e, w = map(int,input().split())
        nodes[s].append([w, e])     # 거리, 도착점 순으로 저장

    # 누적거리 저장
    distance = [float('INF') for _ in range(N + 1)]

    def dijkstra(start):
        pq = []
        heapq.heappush(pq,(0, start))
        distance[start] = 0
        
        while pq:
            dist, now = heapq.heappop(pq)
            if distance[now] < dist:
                continue

            for next in nodes[now]:
                next_node = next[1]
                cost = next[0]
                new_cost = dist + cost
                if distance[next_node] <= new_cost:
                    continue
                distance[next_node] = new_cost
                heapq.heappush(pq,(new_cost, next_node))
    dijkstra(0)
    print(f'#{tc} {distance[N]}')