# 1022번 백준 소용돌이 예쁘게 출력하기


# 반시계 모양
dir = [(0, 1), (-1, 0), (0, -1), (1, 0)]
r1, c1, r2, c2 = map(int,input().split())
n = 2 * max(abs(r1), abs(r2), abs(c1), abs(c2))
arr = [[0 for _ in range(n)] for _ in range(n)]

# 좌표들 중 최대값 기준으로 최대 x 최대 행렬을 만들어줄까?
while True:
    d = 0  # 방향의 idx값

