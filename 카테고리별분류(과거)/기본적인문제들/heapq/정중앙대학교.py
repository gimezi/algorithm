# 정중앙 대학교
'''
가운데 값 찾기

'''
from heapq import heappop, heappush, heapify

N = int(input())
left = []
right = []
mid = 500
for _ in range(N):
    a, b = map(int,input().split())
    for num in (a, b):
        if num > mid:
            heappush(right, num)
        else:
            heappush(left, -num)

    while True:
        if len(right) == len(left):
            print(mid)
            break
        elif len(right) > len(left):
            a = heappop(right)
            if mid > 0:
                mid *= -1
            heappush(left, mid)
            mid = a
        elif len(left) > len(right):
            a = heappop(left)
            if a < 0:
                a *= -1
            heappush(right, mid)
            mid = a
