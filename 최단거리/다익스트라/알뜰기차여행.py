# SWEA 알뜰기차여행
# 다익스트라
'''
아래 그래프에는 이동 경로마다 기차 비용이 적혀있습니다.
출발 지점에서 도착지점까지 가장 저렴한 방법으로 이동하려고 합니다.
아영이 커플을 위해,가장 저렴한 노선의 비용을 알려주는 프로그램을 제작해 주세요.(시러요)


0번 노드에서 출발하여 N - 1 노드에 도착해야 합니다.
이때, 가장 저렴하게 갈수 있는 비용을 출력해 주세요.
만약 갈수 있는 길이 없다면, "impossible" 을 출력합니다.
'''
import heapq

N, T = map(int,input().split())
arr = [[] for _ in range(N + 1)]
for _ in range(T):
    a, b, w = map(int,input().split())
    arr[a].append([b, w])

def train(start):
    pq = []
    heapq.heappush(pq, (start, 0))
    distance = [float('INF') for _ in range(N + 1)]
    distance[start] = 0
    cnt = 0
    while pq:
        now, dis = heapq.heappop(pq)
        cnt += 1
        if distance[now] < dis:
            continue
        for next in arr[now]:
            nextnode = next[0]
            nextcost = next[1] + dis
            if distance[nextnode] < nextcost:
                continue
            distance[nextnode] = nextcost
            heapq.heappush(pq, (nextnode, nextcost))

    if cnt == T:
        return distance[N - 1]
    else:
        return 'impossible'
    
print(train(0))
    