# 예식장 서빙

'''
테이블에 앉은 모든 사람들 기준으로 앉아서 먹을 수 있는 음식들이 
2개 까지만 중복되게끔 서빙 되있더다면 YES를, 그렇지 않다면 NO를 출력 해 주세요.

첫 번째 줄에 테스트 케이스의 수 T 가 주어집니다. (1 <= T <= 100)
각 테스트 케이스의 첫 번째 줄에는 두 정수 N, R 이 주어집니다. (1 <= N <= 1,000,000) (1 <= R <= 50,000)
각 테스트 케이스의 두 번째 줄에는 N 개의 음식이 숫자로 띄어쓰기로 구분되어 주어집니다. (숫자의 범위는 0 ~ 200 입니다)
모든 테스트케이스의 음식들 개수를 합한 값은 20,000,000을 넘지 않습니다.

[입력]
2
7 2
65 66 81 86 65 71 82
8 2
65 65 81 66 65 65 69 69

[출력]
#1 YES
#2 NO
'''
# 강사님 코드

foods = list(map(int, input().split()))
arr = foods * 2
DAT = [0] * 201
# 서빙 성공 여부 탐색 구간의 길이 -> 2 * R + 1
start = 0
end = 2 * R
flag = 0  # 서빙 성공 여부
# 첫번째 구간 탐색
for k in range(start, end):
    DAT[arr[k]] += 1
    if DAT[arr[k]] > 2:
        flag = 1
        break
# 슬라이딩 윈도우 기법
# end포인터가 리스트의 끝에 도착하거나, flag가 1이되면 종료
while end < 2 * N and flag == 0:
    DAT[arr[end]] += 1
    if DAT[arr[end]] > 2:
        flag = 1
        break
    # start포인터가 가리키는 요소의 빈도 1감소
    DAT[arr[start]] -= 1
    start += 1
    end += 1








# 내꺼


def check(arr):
    food_dict = {}
    for food in arr:
        try:
            food_dict[food] += 1
        except:
            food_dict[food] = 1
    for nums in food_dict.values():
        if nums >= 3:
            return False
        else:
            return True

T = int(input())
for tc in range(1, T + 1):
    N, R = map(int,input().split())
    table = list(map(int,input().split()))
    R = 2 * R + 1
    is_true = True
    sub1 = table[:R]
    for i in range(N):
        if check(sub1):
            if i < N - R:
                sub1.append(table[R + i])
                sub1.pop(0)
            else:
                sub1.append(table[R + i - N])
                sub1.pop(0)
        else:
            is_true = False
            break
    if is_true:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')
    
    