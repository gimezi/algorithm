# 1026번 보물
'''
S = A[0] x B[0] + ... + A[N-1] x B[N-1]
S의 값을 가장 작게 만들기 위해 A의 수를 재배열하자. 
단, B에 있는 수는 재배열하면 안 된다.

[입력]
5
1 1 1 6 0
2 7 8 3 1

[출력]
S의 최소값

18
'''
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort(reverse=True)
B.sort()

S = 0
for i in range(N):
    S += A[i] * B[i]
print(S)