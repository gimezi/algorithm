# 액체괴물놀이
'''
여러 마리의 액체괴물들을 합성하여, 하나의 궁극의 액괴를 만들려고한다
A, B kg 짜리 두개를 합칠때 A + B 시간이 걸린다


1차 합성 : 3, 3, 4, 5 (1 + 2 = 3시간 소요)
2차 합성 : 6, 4, 5 (3 + 3 = 6시간 소요)
3차 합성 : 6, 9 (4 + 5 = 9시간 소요)
4차 합성 : 15 (6 + 9 = 15시간 소요)
최소시간은 3 + 6 + 9 + 15 = 33 시간이 걸린다.
[입력]
5
3 2 10 7 6

[출력]
61
'''

# N = int(input())
# arr = list(map(int,input().split()))
# result = 0
# while len(arr) > 1:
#     arr.sort()
#     mult = arr[0] + arr[1]
#     result += mult
#     arr = arr[2:]
#     arr.append(mult)
# print(result)










# heapq
'''
import heapq
 
N = int(input())
arr = list(map(int, input().split()))
 
heapq.heapify(arr)
 
total = 0
 
while len(arr) > 1:
    A = heapq.heappop(arr)
    B = heapq.heappop(arr)
     
    new_heapq = A + B
    total += new_heapq
     
    heapq.heappush(arr, new_heapq)
 
print(total)
'''





# 우선순위 큐
import heapq
pq = []
N = int(input())
nums = list(map(int,input().split()))

for num in nums:
    heapq.heappush(pq, num)

sumv = 0
while len(pq) > 1:
    a = heapq.heappop(pq)
    b = heapq.heappop(pq)
    c = a + b  
    sumv += c
    heapq.heappush(pq, c)

print(sumv)