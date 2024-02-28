# 백준
# 구간 합 구하기

'''
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)과 M(1 ≤ M ≤ 10,000), 
K(1 ≤ K ≤ 10,000) 가 주어진다.
M은 수의 변경이 일어나는 횟수이고, K는 구간의 합을 구하는 횟수이다. 
그리고 둘째 줄부터 N+1번째 줄까지 N개의 수가 주어진다. 
그리고 N+2번째 줄부터 N+M+K+1번째 줄까지 세 개의 정수 a, b, c가 주어지는데,
a가 1인 경우 b(1 ≤ b ≤ N)번째 수를 c로 바꾸고 
a가 2인 경우에는 b(1 ≤ b ≤ N)번째 수부터 c(b ≤ c ≤ N)번째 수까지의 
합을 구하여 출력하면 된다.
입력으로 주어지는 모든 수는 -263보다 크거나 같고,
263-1보다 작거나 같은 정수이다.

5 2 2
1
2
3
4
5
1 3 6
2 2 5
1 5 2
2 3 5
'''

import sys
input = sys.stdin.readline

# 세그먼트 트리 만들기
def Create(seg, node, left, right):
    if left == right:
        seg[node] = arr[left]
        return seg[node]
    mid = left + (right - left) // 2
    left_value = Create(seg, 2 * node, left, mid)
    right_value = Create(seg, 2 * node + 1, mid + 1, right)
    seg[node] = left_value + right_value
    return seg[node]

def Update(idx, val, node, left, right):
    if idx < left or idx > right:
        return seg[node]
    if left == right:
        seg[node] = val
        return seg[node]
    
    mid = left + (right - left) // 2
    left_value = Update(idx, val, 2 * node, left, mid)
    right_value = Update(idx, val, 2 * node + 1, mid + 1, right)
    seg[node] = left_value + right_value
    return seg[node]


# 구간 합 출력하기
def PrintSum(start, end, node, left, right):
    # 범위가 넘어가면 0출력
    if end < left or start > right:
        return 0
    
    # 담당구역 전체가 포함되는 경우 바로 리턴해준다
    if start <= left and right <= end:
        return seg[node]
    mid = left + (right - left) // 2
    left_value = PrintSum(start, end, 2 * node, left, mid)
    right_value = PrintSum(start, end, 2 * node + 1, mid + 1, right)
    return left_value + right_value

N, M, K = map(int,input().split())
arr = [0]

for _ in range(N):
    num = int(input())
    arr.append(num)

# 세그먼트 트리
seg = [0 for _ in range(4 * len(arr))]
Create(seg, 1, 0, len(arr) - 1)

while True:
    try:
        a, b, c = map(int,input().split())
    except:
        break
    if a == 1:
        # 숫자바꾸기
        Update(b, c, 1, 0, len(arr) - 1)
    else:
        # 구간 합 출력하기
        print(PrintSum(b, c, 1, 0, len(arr) - 1))