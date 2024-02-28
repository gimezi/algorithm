# 슈퍼마리오

'''
마리오는 2칸 또는 7칸을 뛸 수 있다.
최고점수를 출력하세요

[입력]
14
1 50 1 -1 1 3 -5 1 -15 0 100 1 1 2

[출력] 
150 


문제 좀 읽어라ㅏㅏ
'''

n = int(input())        # 맵사이즈
MAP = list(map(int, input().split()))
MAP.insert(0,0)
MAP.append(0)

DP = [0 for _ in range(n + 2)]

def jumping(num):
    if DP[num] != 0:
        return DP[num]
    if num <= 0:
        return 0
    elif num < 7:
        if not num % 2: # 7보다 작은 짝수이면, 자기 + 2작은거
            DP[num] = MAP[num] + jumping(num - 2)
        else:
            DP[num] = 0   # 7보다 작은 홀수는 갈 수 없음
    elif num == 7:
        DP[num] = MAP[num]
    else:
        DP[num] = MAP[num] + max(jumping(num - 2), jumping(num - 7)) 
    
    return DP[num]

for i in range(1, n + 1):
    jumping(i)
print(max(DP))