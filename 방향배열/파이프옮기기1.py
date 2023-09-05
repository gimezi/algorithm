# 17070번 파이프 옮기기

'''
유현이가 새 집으로 이사했다. 새 집의 크기는 NxN의 격자판으로 나타낼 수 있고, 
1x1크기의 정사각형 칸으로 나누어져 있다. 각각의 칸은 (r, c)로 나타낼 수 있다. 
여기서 r은 행의 번호, c는 열의 번호이고, 행과 열의 번호는 1부터 시작한다. 
각각의 칸은 빈 칸이거나 벽이다.
오늘은 집 수리를 위해서 파이프 하나를 옮기려고 한다. 
파이프는 2개의 연속된 칸을 차지하는 크기이다.

파이프를 밀 수 있는 방향은 총 3가지가 있으며, →, ↘, ↓ 방향이다. 
파이프는 밀면서 회전시킬 수 있다.

첫째 줄에 파이프의 한쪽 끝을 (N, N)으로 이동시키는 방법의 수를 출력한다. 
이동시킬 수 없는 경우에는 0을 출력한다. 
방법의 수는 항상 1,000,000보다 작거나 같다.

[입력]
3
0 0 0
0 0 0
0 0 0


6
0 0 0 0 0 0
0 1 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0


[출력]
1

13
'''
'''
현재 상태에 따라 갈 수 있는 방향이 달라진다
'''

# 가로 0
dir1 = [(0, 1), (0, 0), (1, 1)]
# 세로 1 
dir2 = [(0, 0), (1, 0), (1, 1)]
# 대각선 2
dir3 = [(0, 1), (1, 0), (1, 1)]

# 합쳐서 한번에 쓸까
dirs = [[(0, 1), (0, 0), (1, 1)], [(0, 0), (1, 0), (1, 1)], [(0, 1), (1, 0), (1, 1)]]

N = int(input())

MAP = [list(map(int,input().split())) for _ in range(N)]

def find(sy, sx, n):        # 시작점 좌표와 방향, (0,1,0)
    stack = [(sy, sx, n)]
    cnt = 0
    while True:
        cy, cx, dire = stack.pop()
        for dy, dx in dirs[dire]:
            ny = cy + dy
            nx = cx + dx
            if 0 <= ny < N and 0 <= nx < N and MAP[ny][nx] == 0:
                if ny == N - 1 and nx == N - 1:
                    cnt += 1
                if dy and dx:
                    stack.append((ny, nx, 2))
                    MAP[ny][nx] = 3
                elif dy:
                    stack.append((ny, nx, 1))
                    MAP[ny][nx] = 3
                else:
                    stack.append((ny, nx, 0))
                    MAP[ny][nx] = 3
        else:
            if stack:
                stack.pop()
            else:
                break
    return cnt

find(0, 1, 0)
