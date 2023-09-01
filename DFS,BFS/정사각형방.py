'''
당신이 어떤 방에 있다면, 상하좌우에 있는 다른 방으로 이동할 수 있다.
물론 이동하려는 방이 존재해야 하고, 
이동하려는 방에 적힌 숫자가 현재 방에 적힌 숫자보다 정확히 1 더 커야 한다.
처음 어떤 수가 적힌 방에서 있어야 가장 많은 개수의 방을 이동할 수 있는지 구하는 프로그램을 작성하라.

2
2
1 2
3 4
3
9 3 4
6 1 5
7 8 2


#1 1 2
#2 3 3
'''
# 강사님코드
for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    v = [0] * (N * N + 1)
    for i in range(N):
        for j in range(N):
            for r, c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if 0 <= i + r < N and 0 <= j + c < N and arr[i][j] + 1 == arr[i + r][j + c]:
                    v[arr[i][j]] = 1
    start, cnt, temp = 0, 1, 1
    for i in range(len(v) - 1, -1, -1):
        if v[i] == 1:
            temp += 1
        else:
            if cnt <= temp:
                cnt = temp
                start = i + 1
            temp = 1
    print(f'#{tc} {start} {cnt}')



## 내꺼

# from collections import deque

# dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]    # 상하좌우 dir

# def BFS(y, x):
#     que = deque([(y, x, 1)])
#     max_level = 0
#     while que:
#         cy, cx, level = que.popleft()
#         if level > max_level:
#             max_level = level

#         for dy, dx in dir:
#             ny, nx = cy + dy, cx + dx
#             if 0 <= ny < N and 0 <= nx < N:
#                 if MAP[cy][cx] + 1 == MAP[ny][nx]:
#                     que.append((ny, nx, level + 1))
    
#     return max_level 


# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     MAP = [list(map(int,input().split())) for _ in range(N)]
#     maxc = 0
#     for i in range(N):
#         for j in range(N):
#             cnt = BFS(i,j)
#             if cnt > maxc:
#                 maxc = cnt
#                 my = i
#                 mx = j
#             elif cnt == maxc:
#                 if MAP[i][j] < MAP[my][mx]:
#                     maxc = cnt
#                     my = i
#                     mx = j
#     print(f'#{tc} {MAP[my][mx]} {maxc}')
