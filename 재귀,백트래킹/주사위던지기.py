# 주사위 던지기
'''
M = 1 : 주사위를 N번 던져서 나올 수 있는 모든 경우
M = 2 : 주사위를 N번 던져서 중복이 되는 경우를 제외하고 나올 수 있는 모든 경우
M = 3 : 주사위를 N번 던져서 모두 다른 수가 나올 수 있는 모든 경우

'''
N, M = map(int,input().split())
arr = []


# M = 1일때
def dice1(N, arr):
    if len(arr) == N:
        print(*arr)
        return
    for i in range(1, 7):
        arr.append(i)
        dice1(N, arr)
        arr.pop()

# M = 2일때
arr2 = []
def dice2(N, arr):
    if len(arr) == N:
        if set(arr) not in arr2:
            arr2.append(set(arr))
            print(*arr)
            return
        return
    for i in range(1, 7):
        arr.append(i)
        dice2(N, arr)
        arr.pop()


# M = 3일때
def dice3(N, arr):
    if len(arr) == N:
        print(*arr)
        return
    for i in range(1, 7):
        if i not in arr:
            arr.append(i)
            dice3(N, arr)
            arr.pop()

if M == 1:
    dice1(N, arr)
elif M == 2:
    dice2(N, arr)
elif M == 3:
    dice3(N, arr)