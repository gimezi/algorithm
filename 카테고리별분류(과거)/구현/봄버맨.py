# 백준 16918번 봄버맨

'''
크기가 R * C인 직사각형 격자판 위
폭탄이 있는 칸은 3초 후에 폭발하고, 이후엔 십자로 파괴된다
근데 만약에 십자에 폭탄이 있다면? 그때는 그칸만 파괴된다(연쇄는 없음)
(파괴 = 빈칸이 됨)

봄버맨은 처음에 일부 칸에 폭탄을 설치하고
1초동안 아무것도 안하고
1초동안 설치 안되어 있는 칸에 폭탄을 설치하고
1초후에 3초전에 설치된 곳이 파괴된다

R개의 줄에 N초가 지난 후의 격자판 상태를 출력
입력은 R, C, N으로 주어지고 초기상태가 주어짐
.은 빈칸 O는 폭탄


그림으로 그려보면 4초를 기준으로 반복됨
나머지가 2, 0초일 때는 그냥 다 차있음
'''

dire = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]

R, C, N = map(int,input().split())
MAP = []
for _ in range(R):
    arr = list(input())
    MAP.append(arr)


flag = N % 4
# N = 0 또는 1이면 초기 상태
if N == 0 or N == 1:
    for i in range(R):
        print(''.join(MAP[i]))
# 나머지가 1일 때는 터진거 구하기
elif flag == 1:
    # 처음꺼 터진거
    tmp1 = [['O' for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if MAP[i][j] == 'O':
                for dy, dx in dire:
                    if 0 <= i + dy < R and 0 <= j + dx < C:
                        tmp1[i+dy][j+dx] = '.'
    # 두번째 터진거
    tmp2 = [['O' for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if tmp1[i][j] == 'O':
                for dy, dx in dire:
                    if 0 <= i + dy < R and 0 <= j + dx < C:
                        tmp2[i+dy][j+dx] = '.'
    for k in range(R):
        print(''.join(tmp2[k]))
# 나머지가 2이랑 0일 때는 다 차있음
elif flag == 2 or flag == 0:
    for i in range(R):
        print('O' * C)
# 나머지가 3일 때는 초기상태에서 십자로 터짐
elif flag == 3:
    result = [['O' for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if MAP[i][j] == 'O':
                for dy, dx in dire:
                    if 0 <= i + dy < R and 0 <= j + dx < C:
                        result[i+dy][j+dx] = '.'
    for k in range(R):
        print(''.join(result[k]))

