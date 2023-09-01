# 6개의 숫자에 대해서 완전 검색으로 babyjin여부 판별하기

# def f(i, N):
#     if i == N:      # 순열 완성
#         return 
#     else:           # p[i]에 들어갈 숫자를 결정
#         for j in range(N):
#             if not used[i]:
#                 p[i] = card[j] 
#                 used[j] = 1
#                 f(i + 1, N)
#                 used[j] = 0


# card = list(map(int,input()))
# used = [0] * 6      # 이미 사용한 카드인지 체크
# p = [] * 6
# f(0,6)









'''
N개 중에 K개만 만들기
'''
# def f(i, N, K):        # N개에서 K개를 고르는 경우
#     if i == K:      # 순열 완성: K개를 모두 고른 경우
#         print(p)
#         return 
#     else:           # p[i]에 들어갈 숫자를 결정
#         for j in range(N):
#             if not used[j]:
#                 p[i] = card[j] 
#                 used[j] = 1
#                 f(i + 1, N, K)
#                 used[j] = 0


# card = [1, 2, 3, 4, 5]
# N = 5
# K = 3
# used = [0] * N   # 이미 사용한 카드인지 체크
# p = [0] * K
# f(0,N, K)



'''
바이너리 리서치를 이용해서 부분집합 만들기
'''
a = [3, 6, 7, 1, 5, 4]
N = 6

for i in range(1, (1 << N) - 1):        # 괄호 잘 쓰기 1<<(N - 1) == (1<<N) // 2
    subset1 = []
    subset2 = []
    for j in range(N):
        if i & (1 << j):    # j번 비트가 0이 아니면
            subset1.append(a[j])
        else:
            subset2.append(a[j])
    print(subset1, subset2)
