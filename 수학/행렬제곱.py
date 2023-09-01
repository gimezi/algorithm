# 10830 행렬 제곱

'''
크기가 N*N인 행렬 A가 주어진다. 이때, A의 B제곱을 구하는 프로그램을 작성하시오. 
수가 매우 커질 수 있으니, A^B의 각 원소를 1,000으로 나눈 나머지를 출력한다.
첫째 줄에 행렬의 크기 N과 B가 주어진다. (2 ≤ N ≤  5, 1 ≤ B ≤ 100,000,000,000)
둘째 줄부터 N개의 줄에 행렬의 각 원소가 주어진다. 
행렬의 각 원소는 1,000보다 작거나 같은 자연수 또는 0이다.

[입력]
2 5
1 2
3 4

[출력]
69 558
337 406
'''

# 함수가 두 개?
# 행렬 제곱하는 함수하나랑
# 분할 정복하는 함수

def mult1(arr1, arr2, N): # arr1과 arr2를 곱해주는 함수, N은 두 arr의 크기
    new_arr = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            ans = 0
            for k in range(N):
                ans += (arr1[i][k] * arr2[k][j])
            new_arr[i][j] += ans % 1000
    return new_arr

def mult2(arr, N): # arr을 제곱해주는 함수, N은 두 arr의 크기
    new_arr = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            ans = 0
            for k in range(N):
                ans += (arr[i][k] * arr[k][j])
            new_arr[i][j] += ans % 1000
    return new_arr

def square(arr, m): # arr는 제곱할 행렬, m은 지수
    if m == 1:
        return arr
    elif m % 2:     # 지수가 홀수면
        return mult1(mult2(square(arr, m // 2), N), arr, N)
    else:
        return mult2(square(arr, m // 2), N)

N, B = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] >= 1000:
            arr[i][j] = arr[i][j] % 1000
result = square(arr, B)
for nums in result:
    print(*nums)


