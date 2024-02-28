# 최대상금
'''
3
123 1
2737 1
32888 2

1
123 1


#1 321
#2 7732
#3 88832

'''
def union(cnt, num):
    num = ''.join(num)  # 우선 합쳐
    if num not in visited[cnt]:  # 중복이 있는지 확인
        visited[cnt].append(num)
    num = list(num)


def find(num, cnt):
    for i in range(len(num) - 1):
        for j in range(i + 1, len(num)):
            num[i], num[j] = num[j], num[i]     # 바꿔요
            union(cnt + 1, num)
            num[j], num[i] = num[i], num[j]     # 원상복귀해줘요

T = int(input())
for tc in range(1, T + 1):
    num, n = input().split()
    n = int(n)
    visited = [[] for _ in range(n + 1)]
    visited[0].append(num)
    for i in range(n):
        for nums in visited[i]:
            nums = list(nums)
            find(nums, i)
    result = list(map(int,visited[n]))
    ans = max(result)
    print(f'#{tc} {ans}')





















# import copy

# def makenum(lst):
#     result = 0
#     for i in range(len(lst)):
#         result += lst[i] * (10 ** (len(lst) - i - 1))
#     return result


# T = int(input())
# for tc in range(1, T + 1):
#     num, n = input().split()
#     n = int(n)
#     num = list(map(int,num))
#     # 부분집합 만들기
#     nlst = []
#     for i in range(1 << len(num)):
#         a = []
#         for j in range(len(num)):
#             if i & (1 << j):
#                 a.append(j + 1)
#                 if len(a) == 2:
#                     if a not in nlst:
#                         nlst.append(a)
#                     break
#     maxv = 0
#     cnt = 1
#     while cnt <= n:
#         for p1, p2 in nlst:
#             newnum = copy.deepcopy(num)
#             newnum[p1 - 1], newnum[p2 -1] = newnum[p2 -1], newnum[p1 - 1]
#             newnum = makenum(newnum)
#             if newnum > maxv:
#                 maxv = newnum
#         cnt += 1
#         num = list(map(int,str(maxv)))
#     print(f'#{tc} {maxv}')

        

