# 베이비진 게임
'''
0부터 9까지인 숫자 카드 4세트를 섞은 후 6개의 카드를 골랐을 때, 
연속인 숫자가 3개 이상이면 run, 같은 숫자가 3개 이상이면 triplet이라고 한다.
게임을 시작하면 플레이어1과 플레이어 2가 교대로 한 장 씩 카드를 가져가며, 
6장을 채우기 전이라도 먼저 run이나 triplet이 되는 사람이 승자가 된다.
두 사람이 가져가게 되는 순서대로 12장의 카드에 대한 정보가 주어졌을 때 
승자를 알아내는 프로그램을 작성하시오. 만약 무승부인 경우 0을 출력한다.
예를 들어 9 9 5 6 5 6 1 1 4 2 2 1인 경우, 플레이어 1은 9, 5, 5, 1, 4, 2카드를,
플레이어2는 9, 6, 6, 1, 2, 1을 가져가게 된다.
이때는 카드를 모두 가져갈 때 까지 run이나 triplet이 없으므로 무승부가 된다.

[입력]
3
9 9 5 6 5 6 1 1 4 2 2 1
5 3 2 9 1 5 2 0 9 2 0 0
2 8 7 7 0 2 2 2 5 4 0 3


[출력]
#1 0
#2 1
#3 2
'''

def run1(arr):
    cnt = 1
    for i in range(len(arr) - 2):
        if arr[i] == arr[i + 1]:
            cnt +=1
            if cnt == 3:
                return 1
        else:
            cnt = 1
    return 0

def triple(arr):
    for num in arr:
        if (num + 1) in arr:
            if (num + 2) in arr:
                return 1
    return 0

def game(tc, arr):        
    A, B = [], []
    for i in range(len(arr) // 2):
        A.append(arr[2 * i])
        A.sort()
        if triple(A) or run1(A):
            print(f'#{tc} 1')
            return
        B.append(arr[2 * i + 1])
        B.sort()
        if triple(B) or run1(B):
            print(f'#{tc} 2')
            return
    print(f'#{tc} 0')
    return


T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int,input().split()))
    game(tc, arr)
    
        
'''
def check_win(cards):
    cnt = [0] * 10
    for num in cards:
        cnt[num] += 1
 
    # run 확인
    if 3 in cnt:
        return True
    
    # triplet 확인
    for i in range(8):
        if 0 not in cnt[i : i + 3]:
            return True

    return False
'''
