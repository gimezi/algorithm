'''
8725 328744
-1

27297 339652
425

34768 292340
-1

438 129118
95

4040 160532
385
'''
import heapq

def find(n, k):
    pq = []
    heapq.heappush(pq, (0, n, k)) # 레벨, 현재 위치, 목표
    check = [0 for _ in range(500001)]
    minlevel = float('INF')

    while pq:
        level, now, goal = heapq.heappop(pq)
        goal += level
        # print(f'차이 = {cha}, level = {level}, 현재위치={now}, 목표= {goal}')
        if now == goal and level < minlevel:
            minlevel = level
        if now == goal and level > minlevel:
            return minlevel
        
        # 가지치기 1. goal이 범위를 넘어갈때
        if goal > 500000:
            return -1
        
        if check[now] == 0:
            for next in [now + 1, now - 1, 2 * now]:
                if 0 < next <= 500000:
                    heapq.heappush(pq, (level + 1, next, goal))
        # 왔다갔다(짝수일때만?)
        check[now] = 1
        heapq.heappush(pq, (level + 2, now, goal))

    return -1


N, K = map(int,input().split())
print(find(N,K))

# from collections import deque

# def find(n, k):
#     que = deque([(n, 0, k)])   # 현재 위치, 레벨, 목표
#     visited = [0 for _ in range(500001)]
#     visited[n] = 1

#     while que:
#         now, level, goal = que.popleft()
#         goal += level
#         # print(now, level, goal)
#         if now == goal:
#             return level
        
#         # 가지치기 1. goal이 범위를 넘어갈때
#         if goal > 500000:
#             return -1
        
#         # 가지치기 2. goal이 현재보다 2배 이상 클때
#         if goal >= now* 2:
#             next = now * 2
#             que.append((next, level + 1, goal))
#         else:
#             for next in [now + 1, now - 1, 2 * now]:
#                 if 0 < next <= 500000 and visited[next] == 0:
#                     visited[next] = 1
#                     que.append((next, level + 1, goal))
#             # 왔다갔다(짝수일때만?)
#             que.append((now, level + 2, goal))
#     return -1


# N, K = map(int,input().split())
# print(find(N,K))

