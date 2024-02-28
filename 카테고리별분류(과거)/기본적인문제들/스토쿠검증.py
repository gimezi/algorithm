#스토쿠 검증

# case개수 받기
N = int(input())

# x라는 리스트를 넣었을때, 한 줄 안에 같은게 있는지 찾는함수
def find_same(x):
    # for i in range(0,8):
    #     x[i].sort() # 순서대로 정렬
    
    # a = 1
    # for i in range(0,8):
    #     if x[i][8] == 9:
    #         continue
    #     else:
    #         a = 0
    # return a
    
    for i in range(0,8):
        check = set(x[i])
        if len(check) == 9:
            a = 1
        else:
            a = 0 
    return a

# input받기
for j in range(1,N+1):

    sudoku = []

    for i in range(1,10):
        data = map(int,input().split())
        data = list(data)
        sudoku.append(data)
    
    # 가로줄
    check1 = sudoku
    a1 = find_same(check1)

    # 세로줄
    check2 = []
    for i in range(0,9):
        check2[i]
    a2 = find_same(check2)

    print("#{} {}".format(j,a2))
