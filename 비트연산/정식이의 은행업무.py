# 스웨아 정식이의 은행 업무
'''
binary = '0b' + binary      # 이진수로 바꿔보기
binary = int(binary, 2)     # 다시 십진수로 바꾸기


1
1010
212

#1 14
'''

T = int(input())
for tc in range(1, T + 1):
    A = input()         # 2진수
    B = list(map(int,input()))   # 3진수
    N = len(A)
    M = len(B)
    ans = 0

    binary = int(A, 2)                 # 2진수를 정수로 변환
    binlst = [0 for _ in range(N)]     # 각 비트를 반전시킨 수 N개를 저장 
    for i in range(N):                 # 각 비트를 반전시긴 2진수 만들기
        binlst[i] = binary ^ (1 << i)
    
    for i in range(M):  # 3진수의 각 자리를 바꾼 숫자 만들기
        num1 = 0
        num2 = 0
        for j in range(M):
            if i != j:
                num1 = num1 * 3 + B[j]
                num2 = num2 * 3 + B[j]
            else:
                num1 = num1 * 3 + (B[j] + 1) % 3
                num2 = num2 * 3 + (B[j] + 2) % 3
        if num1 in binlst:
            ans = num1
            break
        if num2 in binlst:
            ans = num2
            break
    print(f'#{tc} {ans}')


