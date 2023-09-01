# SWEA 회문

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    numslst = [list(input()) for _ in range(N)]


    # for row in numslst:
    #     for i in range(0, N - M + 1):
    #         lst1 = []
    #         for j in range(i, M):
    #             lst1.append(row[j])
    #         print(lst1)
            

    # 가로로 먼저 찾기
    # 잘라서 만든 다음에 회문인지 판별하기

    for row in numslst:
        for i in range(0, N - M + 1):
            lst1 = []
            for j in range(M):
                lst1.append(row[j + i])
            lst2 = lst1[::-1]
            cnt = 0
            for l in range(M):
                if lst1[l] == lst2[l]:
                    cnt += 1
            if cnt == M:
                print(f'#{tc}',''.join(lst1))

    # 세로로 찾기
    # 얘도 잘라서 만들고 회문인지 판별하기
    for i in range(N):
        for k in range(0, N - M + 1):
            lst3 = []
            for j in range(M):
                lst3.append(numslst[j + k][i])
            lst4 = lst3[:: -1] 
            cnt = 0
            for l in range(M):
                if lst3[l] == lst4[l]:
                    cnt += 1
            if cnt == M:
                print(f'#{tc}',''.join(lst3))         
            