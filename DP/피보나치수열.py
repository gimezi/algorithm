# 피보나치 수열
'''

피보나치 수열은 0 1 부터 시작되고,
다음 수는 이전 값과, 이전의 이전값의 과 전전의 값의 합으로 만들어집니다.
피보나치 수열을 나열하면 다음과 같습니다.
0 1 1 2 3 5 8 ...
네 번째 (n = 4) 피보나치 수열은 2 입니다.
n을 입력받고, n 번째 피보나치 값을 출력하는 프로그램을 작성해 주세요.
[제한조건]
1 <= n <= 35

'''


n = int(input())
fibo = [0 for _ in range(n)]    # 0 ~ n - 1까지의 칸

def find(n):
    if fibo[n]:
        return fibo[n]

    if n == 0:
        fibo[n] = 0
    elif n == 1:
        fibo[n] = 1
    else:
        fibo[n] = find(n - 1) + find(n - 2)
    return fibo[n]

print(find(n - 1))
