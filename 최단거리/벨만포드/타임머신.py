# 타임머신 (벨만 포드)

'''
N개의 도시가 있고, 버스가 M개 있다.
A에서 B도시로 가고 C는 각각 걸리는 시간이다.
C는 0이거나 음수도 가능하다
1번 도시부터 출발해서 나머지 도시로 가는 가장 빠른 시간을 구하는 프로그램 작성하세요

-> 우선 음수도 가능하므로 다익스트라는 안됨
벨만-포드 알고리즘을 사용하자

'''

N, M = map(int,input().split())
# 간선 정보 리스트
bus = []
# 최단거리 저장할 리스트
dis = [float('inf') for _ in range(N + 1)]
dis[1] = 0      # 시작점은 거리 0

for _ in range(M):
    a, b, c = map(int,input().split())
    bus.append((a, b, c))

# 음수사이클 판별용
isNegativeCycle = False

# 벨만포드알고리즘
for i in range(N):
    # 모든 간선을 체크
    for j in range(M):
        now, next, cost = bus[j]
        # 지금이 무한이 아니고, 현재에 cost 더한게 저장되어있는거보다 작다면 업데이트
        if dis[now] != float('inf') and dis[next] > dis[now] + cost:
            dis[next] = dis[now] + cost
            # 음수사이클 판별용
            if i == N - 1:
                isNegativeCycle = True

if isNegativeCycle:
    print(-1)
else:
    for idx in range(2, N + 1):
        if dis[idx] != float('inf'):
            print(dis[idx])
        else:
            print(-1)