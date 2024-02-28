# 최소 생산 비용

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    fee = []
    for _ in range(N):
        a = list(map(int,input().split()))
        fee.append(a)
    factory = [0 for _ in range(N)]

    minv = float('INF')
    
    def manuf(k, cnt):  # k번 제품, cnt는 총 가격
        global minv
        if k == N:
            if cnt < minv:
                minv = cnt
                return
        for i in range(N):
            if factory[i] == 0:
                val = fee[k][i]
                if cnt + val < minv:
                    factory[i] = 1
                    manuf(k + 1, cnt + val)
                    factory[i] = 0

    manuf(0, 0)
    print(f'#{tc} {minv}')