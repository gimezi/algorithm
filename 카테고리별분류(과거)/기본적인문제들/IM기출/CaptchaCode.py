# Captcha Code
'''
[1] 랜덤으로 N개 길이의 Sample이 주어진다.
[2] 그리고 K개 길이의 PassCode가 주어진다.
[3] 사용자는 Sample에서 PassCode를 "순차적으로" 만들 수 있는지를 검증해야 한다. 

[input]
2
10 4
1 1 2 2 3 3 4 4 5 5
1 2 3 4
7 4
1 2 2 4 3 3 4
4 3 2 1

[output]
#1 1
#2 0
'''


def findpass(nums, key):
    i = 0
    while True:
        if key:
            if nums[i] == key[0]:
                key.pop(0)
            i += 1
            if i == len(nums) - 1:
                return 0
        else:
            return 1
    

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    num = list(map(int, input().split()))
    password = list(map(int, input().split()))
    result = findpass(num, password)
    print(f'#{tc} {result}')