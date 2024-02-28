# 구간의 합
'''
수열이 주어질때, 연속한 구간의 합이 M이 되는 갯수를 구하는 프로그램

첫번째 줄에 N(1 ≤ N ≤ 10,000), M(1 ≤ M ≤ 300,000,000)이 주어집니다.
다음 줄에는 A[1], A[2], …, A[N]이 공백으로 분리되어 주어집니다. 
각각의 A[x]는 30,000을 넘지 않는 자연수입니다.

[입력]
10 5
1 2 3 4 2 5 3 1 1 2

[출력]
3

'''


N, M = map(int, input().split())
arr = list(map(int, input().split()))

p1, p2 = 0, 0
cnt, sums = 0, 0
while True:
    if sums >= M or p2 == N:
        sums -= arr[p1]
        p1 += 1
    elif sums < M:
        sums += arr[p2]
        p2 += 1
    if sums == M:
        cnt += 1
    if p1 == N:
        break
print(cnt)