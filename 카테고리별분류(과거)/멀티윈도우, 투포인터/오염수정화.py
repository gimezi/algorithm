# 오염수 정화
'''
행렬에서 두개 골라서 더한게 0에 제일 가까운거 찾기

[입력]
5
-2 4 -99 -1 98

[출력]
-99 98
'''


# 강사님
n = int(input())
arr = list(map(int,input().split()))
arr.sort()
left = 0
right = n - 1
minimum = 2e9 + 1
ansleft = 0
ansright = 0

while left < right:
    sums = arr[left] + arr[right]
    if sums == 0:
        print(arr[left], arr[right])
        exit()  # 프로그램 자체를 종료해버림

    if minimum > abs(sum):
        minimum = abs(sum)
        ansleft = left
        ansright = right
    if sum > 0: right -= 1
    else: left += 1

print(arr[ansleft], arr[ansright])




# 내꺼
# N = int(input())
# arr = list(map(int,input().split()))
# minv = float("inf")
# p1, p2 = 0, 0
# for i in range(N):
#     for j in range(i + 1, N):
#         sums = arr[i] + arr[j]
#         if sums == 0 and abs(arr[i]) + abs(arr[j]) > abs(p1) + abs(p2):
#             p1, p2 = arr[i], arr[j]

#         elif abs(sums) <= minv:
#             minv = sums
#             p1, p2 = arr[i], arr[j]

# if p1 <= p2:
#     print(p1, p2)
# else:
#     print(p2, p1)