# 백준 2580번 스토쿠
from pprint import pprint


'''
0 0 0 0 0 0 0 0 9 
0 0 0 0 0 0 0 0 8
0 0 0 0 0 0 0 0 7
0 0 0 0 0 0 0 0 6
0 0 0 0 0 0 0 0 5
0 0 0 0 0 0 0 0 4
0 0 0 0 0 0 0 0 3
0 0 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0 1
'''
import copy

centers = [[(1, 1), (1, 4), (1, 7)], [(4, 1), (4, 4), (4, 7)], [(7, 1), (7, 4), (7, 7)]]
dir = [(0, 0), (1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]

# num가 arr의 y, x자리에 들어가도 되는지?
def check(arr, y, x, num):
    # 네모확인용 센터
    center = centers[y // 3][x // 3]
    # 가로
    if num in arr[y]:
        return False
    # 세로

    for k in range(9): 
        if arr[k][x] == num:
            return False
    # 네모
    for dy, dx in dir:
        if arr[center[0] + dy][center[1] + dx] == num:
            return False
    return True


def sudoku(arr, y, x, t):
    if t == len(zeros) - 1:
        return arr
    #  만약 지금 넣으려고 하는 곳이 이미 채워졌다면
    if arr[y][x] != 0:
        return 

    for i in range(1, 10):
        if check(arr, y, x, i):
            arr[y][x] = i
            visited[y][x][i - 1] = 1
            for ny, nx in zeros:
                if visited[ny][nx][i - 1] == 0:
                    sudoku(arr, ny, nx, t + 1)
            arr[y][x] = 0
        
     
board = [list(map(int,input().split())) for _ in range(9)]
zeros = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            zeros.append((i, j))
visited = [[[0 for _ in range(9)] for _ in range(9)] for _ in range(9)]
sudoku(board, zeros[0][0], zeros[0][1], 0)





# # 9개 칸
# kan = [(1, 1), (1, 4), (1, 7), (4, 1), (4, 4), (4, 7), (7, 1), (7, 4), (7, 7)]
# dir = [(0, 0), (1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
# def sudoku(arr):
#     flag = 0
#     for i in range(9):
#         if 0 not in arr[i]:
#             flag += 1
#     if flag == 9:
#         for i in range(9):
#             print(*arr[i])
#         exit()

#     # 가로부터 
#     for row in range(9):
#         zeros = []
#         nums = [0 for _ in range(9)]
#         for idx in range(9):
#             if arr[row][idx] == 0:
#                 zeros.append(idx)   # 어느 칸이 비었는지 체크해주기
#             else:
#                 nums[arr[row][idx] - 1] += 1 # 나중에 어느 번호가 없는지 확인용 
#         # 만약 비어있는게 한개라면 그냥 넣어줘
        
#         if len(zeros) == 1:
#             # 어떤 숫자가 없었는지 확인해주기
#             for i in range(9):
#                 if nums[i] == 0:
#                     this = i + 1
#             arr[row][zeros[0]] = this
#         # 만약 비어있는게 여러개라면
#         elif len(zeros) > 1:
#             # 없는 숫자 찾아
#             no = []
#             for i in range(9):
#                 if nums[i] == 0:
#                     no.append(i + 1)
#             # 비어있는 칸에 대해서
#             for num in zeros:
#                 # 없는 숫자 한개씩 넣어보기
#                 for n in no:
#                     arr[row][num] = n
#                     sudoku(arr)
#                     arr[row][num] = 0


#     # 세로로 채우기
#     for col in range(9):
#         zeros = []
#         nums = [0 for _ in range(9)]
#         for idx in range(9):
#             if arr[idx][col] == 0:
#                 zeros.append(idx)   # 어느 칸이 비었는지 체크해주기
#             else:
#                 nums[arr[idx][col] - 1] = 1 # 나중에 어느 번호가 없는지 확인용
#         # 비어있는게 한개라면 그냥 넣어주고
#         if len(zeros) == 1:
#             # 어떤 숫자가 없었는지 확인해주기
#             for i in range(9):
#                 if nums[i] == 0:
#                     this = i + 1
#             arr[zeros[0]][col] = this
#         ## 만약 비어있는게 여러개 있다면
#         elif len(zeros):
#             # 없는 숫자 찾아
#             no = []
#             for i in range(9):
#                 if nums[i] == 0:
#                     no.append(i + 1)
#             # 비어있는 칸에 대해서
#             for num in zeros:
#                 # 없는 숫자 한개씩 넣어보기
#                 for n in no:
#                     arr[num][col] = n
#                     sudoku(arr)
#                     arr[num][col] = 0

#     # 9개 칸
#     for cy, cx in kan:
#         zeros = []
#         nums = [0 for _ in range(9)]
#         for dy, dx in dir:
#             ny, nx  = cy + dy, cx + dx
#             if arr[ny][nx] == 0:
#                 zeros.append((ny,nx))
#             else:
#                 nums[arr[ny][nx] - 1] = 1
#         if len(zeros) == 1:
#             for i in range(9):
#                 if nums[i] == 0:
#                     this = i + 1
#             arr[zeros[0][0]][zeros[0][1]] = this
#         # 만약 비어있는게 있다면
#         elif len(zeros):
#             # 없는 숫자 찾아
#             no = []
#             for i in range(9):
#                 if nums[i] == 0:
#                     no.append(i + 1)
#             # 비어있는 칸에 대해서
#             for y, x in zeros:
#                 # 없는 숫자 한개씩 넣어보기
#                 for n in no:
#                     arr[y][x] = n
#                     sudoku(arr)
#                     arr[y][x] = 0


# board = [list(map(int,input().split())) for _ in range(9)]
# sudoku(board)


