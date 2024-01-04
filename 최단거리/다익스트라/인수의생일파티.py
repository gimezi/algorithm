# 인수의 생일 파티
'''
1
4 8 2
1 2 4
1 3 2
1 4 7
2 1 1
2 3 5
3 1 2
3 4 4
4 2 3


#1 10
'''
import heapq

def cele(start, goal):
    pq = []
    heapq.heappush(pq,(0, start))
    times = [float('INF') for _ in range(N + 1)]
    while pq:
        t, now = heapq.heappop(pq)
        # print(t, now, times)
        if now == goal:
            return times[goal]
        if times[now] < t:
            continue
        for next in arr[now]:
            next_house = next[1]
            next_time = t + next[0]
            if next_time >= times[next_house]:
                continue
            times[next_house] = next_time
            heapq.heappush(pq,(next_time, next_house))
    return times[goal]
T = int(input())
for tc in range(1, T + 1):
    N, M, X = map(int,input().split())
    arr = [[] for _ in range(N + 1)]
    for _ in range(M):
        x, y, c = map(int,input().split())
        arr[x].append([c, y])   # 거리, 도착지

    # N번째 집에서 왔다갔다하는데 걸리는 시간 구하기
    ans = []
    for i in range(1, N + 1):
        if i != X:
            a = cele(i,X)    
            b = cele(X,i)
            ans.append(a + b)
    print(f'#{tc} {max(ans)}')

