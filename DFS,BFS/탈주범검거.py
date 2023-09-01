'''
룩업테이블: 미리 계산된 값을 저장해 놓은 테이블(리스트) => 계산 시간을 줄이고, 코드를 간결하게 할 수 있음
'''
'''
5 6 2 1 3      
0 0 5 3 6 0
0 0 2 0 2 0
3 3 1 3 7 0
0 0 0 0 0 0
0 0 0 0 0 0
'''

from collections import deque

# 파이프 모양별로 4방향 연결 가능 여부 나타내는 리스트 (상, 하, 좌, 우)
pipe = [[0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 0, 1], [0, 1, 0, 1], [0, 1, 1, 0], [1, 0, 1, 0]]
# 상, 하, 좌, 우 이동을 위한 dir
di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
# 상하, 좌우 매칭하기 위한 리스트
opp = [0, 1, 2, 3]

def pip(y,x):       # 파이프의 좌표가 주어졌을 때, 갈 수 있는 좌표를 주는 함수
    result = []
    pipedir = pipe[MAP[y][x]]
    for i in range(4):
        if pipedir[i]:
            newy = y + di[opp[i]]
            newx = x + dj[opp[i]]
            result.append((newy, newx))
    return result

def Hodadac(y,x):
    que = deque([(y, x, 1)])
    visited[y][x] = 1

    while que:
        cy, cx, level = que.popleft()
        pipdir = pip(cy, cx)
        if level == L:              # 만약 시간이 넘어가면 종료
            return    
        for ny, nx in pipdir:
            if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == 0:
                if (cy, cx) in pip(ny, nx):
                    visited[ny][nx] = 1
                    que.append((ny, nx, level + 1))


T = int(input())
for tc in range(1, T + 1):
    # N, M: 지도의 가로세로길이 / R, C: 뚜껑위치 / L : 탈출 후 소요된 시간
    N, M, R, C, L = map(int,input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]

    Hodadac(R, C)
    result = 0
    for arr in visited:
        result += sum(arr)

    print(f'#{tc} {result}')
            
        