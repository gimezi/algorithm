'''
10 5
1 2 2 2 2 3 4 3 4 -1
2 3
-1000000000 1000000000
-10 0
2 4
2 2
'''



# def binary_search_recursive1(low, high, target):
#     # 재귀호출을 반복하지 않을 조건
#     if low >= high:
#         if arr[low] < target:
#             return low + 1
#         else:
#             return low

#     mid = (low + high) // 2
#     # arr에서 범위의 최솟값과 일치하는 가장 앞쪽 인덱스를 찾아라
#     if target == arr[mid]:
#         return binary_search_recursive1(0, mid - 1, target)
#         # return mid

#     elif arr[mid] < target:
#         return binary_search_recursive1(mid + 1, high, target)
#     else:
#         return binary_search_recursive1(low, mid - 1, target)

# def binary_search_recursive2(low, high, target):
#     # 재귀호출을 반복하지 않을 조건
#     if low >= high:
#         if arr[high] > target:
#             return high - 1
#         else:
#             return high

#     mid = (low + high) // 2 # 범위가 두 칸이면 앞의 값
#     # arr에서 범위의 최솟값과 일치하는 가장 앞쪽 인덱스를 찾아라
#     if target == arr[mid]:
#         return binary_search_recursive2(mid + 1, high, target)
#         # return mid

#     elif arr[mid] < target:
#         return binary_search_recursive2(mid + 1, high, target)
#     else:
#         return binary_search_recursive2(low, mid - 1, target)


# N, Q = map(int, input().split())
# arr = list(map(int, input().split()))
# arr.sort()
# needs = []

# for _ in range(Q):
#     a, b = map(int, input().split())
#     needs.append((a, b))
# for i, j in needs:
#     min_i = binary_search_recursive1(0, len(arr)-1, i)
#     max_i = binary_search_recursive2(0, len(arr)-1, j)
#     print(max_i-min_i+1)

















# N, Q = map(int,input().split())
# have = list(map(int,input().split()))
# have.sort()
# minv = have[0]
# maxv = have[N - 1]

# for _ in range(Q):
#     v1, v2 = map(int,input().split())
#     if v1 <= minv and v2 >= maxv:
#         result = N
        
#     elif v1 <= minv and v2 < maxv:
#         for i in range(N):
#             if have[i] >= v2:
#                 result = i
#                 break
#     elif v1 > minv and v2 >= maxv:
#         for i in range(N):
#             if have[i] >= v1:
#                 result = N - i

#                 break
#     else:
#         for i in range(N):
#             if have[i] >= v1:
#                 i1 = i
#                 break
#         for j in range(N):
#             if have[j] <= v2:
#                 i2 = j
#         result = i2 - i1 + 1
#     print(result)







def count_minerals(minerals, target):
    left, right = 0, len(minerals) - 1
    while left <= right:
        mid = (left + right) // 2
        if minerals[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    return left

N, Q = map(int, input().split())
minerals = list(map(int, input().split()))
minerals.sort()

for _ in range(Q):
    Si, Ei = map(int, input().split())
    count1 = count_minerals(minerals, Ei)
    count2 = count_minerals(minerals, Si - 1)
    result = count1 - count2
    print(result)