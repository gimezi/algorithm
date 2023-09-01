# SWEA 삼성시의 버스 노선

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    bus_stop = [0] * 5001       # 0부터 시작하니까 5001 까지 해야댐
    for j in range(N):
        bus_start, bus_end = map(int, input().split())
        bus = list(range(bus_start, bus_end + 1))
        for stop in bus:
            bus_stop[stop] += 1
    
    P = int(input())
    C = []
    for j in range(P):
        C.append(int(input()))
    
    result = []
    for c in C:
        result.append(bus_stop[c])
    
    print(f'#{tc}',*result)


