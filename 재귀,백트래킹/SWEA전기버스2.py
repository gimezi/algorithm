# SWEA 전기버스2
'''
충전지를 교환하는 방식의 전기버스를 운행하려고 한다. 
정류장에는 교체용 충전지가 있는 교환기가 있고,
충전지마다 최대로 운행할 수 있는 정류장 수가 정해져 있다.
충전지가 방전되기 전에 교체하며 운행해야 하는데 교체하는 
시간을 줄이려면 최소한의 교체 횟수로 목적지에 도착해야 한다.
정류장과 충전지에 대한 정보가 주어질 때, 
목적지에 도착하는데 필요한 최소한의 교환횟수를 출력하는 프로그램을 만드시오. 
단, 출발지에서의 배터리 장착은 교환횟수에서 제외한다.


[입력]
3
5 2 3 1 1
10 2 1 3 2 2 5 4 2 1
10 1 1 2 1 2 2 1 2 1

[출력]
#1 1
#2 2
#3 5

'''


# 재귀로 품

def bus(now, cnt):   # now = 현재위치, cnt = 교환횟수
    global mincnt
    if now == N - 1:
        if cnt < mincnt:
            mincnt = cnt
        return
    for i in range(1, arr[now] + 1):
        next = now + i
        if next < N:
            if cnt < mincnt:
                bus(next, cnt + 1)


T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int,input().split()))
    N = arr.pop(0)
    mincnt = float('INF')
    bus(0, 0)
    print(f'#{tc} {mincnt - 1}')




# 강사님 코드(DFS)

def dfs(idx, sumv):
    global answer
    if answer < sumv: return
    if idx >= N:
        answer = sumv
        return 
    count = station[idx]
    for i in range(count, 0, -1):
        dfs(idx + i, sumv + 1)

T = int(input())
for tc in range(1, T + 1):
    answer = float('INF')
    station = list(map(int,input().split()))
    N = station.pop(0) - 1
    dfs(0, -1)
