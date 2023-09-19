# N castle
'''
N x N 체스판에 N 개의 캐슬을 배치시켜 나올 수 있는 경우의 수를 출력해주세요
단, 배치할때 서로 공격하지 않아야합니다. 
만약 Castle을 배치해서 이동할 수 있는 곳에 또 다른 Castle이 있다면, 
이는 공격가능한걸로 간주합니다.
아래 이미지는 N = 4 인 경우, 가능한 배치의일부입니다.
'''


# 걍 재귀(팩토리얼)로 풀었음
N = int(input())

def fact(N):
    if N == 1:
        return 1
    return N * fact(N - 1)

print(fact(N))


# 백트래킹으로 풀기
N = int(input())
DAT = [0] * 10
cnt = 0
def func(row):
    global cnt
    # N - 1번행까지 모두 castle을 각 행에 두었다면
    if row == N:
        cnt += 1
        return
    for col in range(N):
        if DAT[col] == 1:   # 이미 이 열에 castle을 둔 적이 있다면
            continue        # 가지치기
        DAT[col] = 1
        func(row + 1)       # 현재를 기반으로 다음 행의 배치를 탐색
        DAT[col] = 0        # 백트래킹: 현재 열의 castle을 둔 것을 해제

func(0)
print(cnt)