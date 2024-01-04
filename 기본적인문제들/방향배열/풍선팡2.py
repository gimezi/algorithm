# SWEA 풍선팡 2
'''
종이 꽃가루가 들어있는 풍선이 NxM 크기의 격자판에 붙어있는데, 
어떤 풍선을 터뜨리면 상하좌우의 풍선이 추가로 터진다고 한다.

NxM개의 풍선에 들어있는 종이 꽃가루 개수A가 주어지면, 
한 개의 풍선을 선택해 터뜨렸을 때 날릴 수 있는 꽃가루 수 중 
최대값을 출력하는 프로그램을 만드시오.
(3<=N, M<=100)


[input]
3
3 5
2 1 1 2 2 
2 2 1 2 2 
2 2 1 1 2 
5 5
3 4 1 2 3 
3 4 1 3 2 
2 3 2 4 1 
1 4 4 1 3 
2 2 3 4 4 
5 8
1 3 4 4 4 4 3 3 
4 1 2 4 3 1 4 4 
4 1 4 4 1 4 2 1 
3 2 4 2 1 1 2 1 
4 4 1 4 4 2 2 2 

[output]
#1 8
#2 16
#3 17

'''


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    

    def pang(y, x):
        dir = [(1, 0), (0, 1), (-1, 0), (0, -1),(0, 0)]
        result = 0
        for dy, dx in dir:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < M:
                result += arr[ny][nx]
        return result
    
    max = 0
    for i in range(N):
        for j in range(M):
            if max <= pang(i, j):
                max = pang(i,j)

    print(f'#{tc} {max}')