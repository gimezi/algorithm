'''
DP가 싫어요 으아악

ACAYKP
CAPCAK

4
ACAK
'''

str1 = input()
str2 = input()

DP = [[0 for _ in range(len(str1) + 1)] for _ in range(len(str2) + 1)]

for i in range(1, len(str2) + 1):
    for j in range(1, len(str1) + 1):
        if str1[j - 1] == str2[i - 1]:
            DP[i][j] = DP[i - 1][j - 1] + 1
        else:
            DP[i][j] = max(DP[i - 1][j], DP[i][j - 1])

result = []
a, b = len(str2), len(str1)
while True:
    if a <= 0 or b <= 0:
        break
    if DP[a][b] == DP[a - 1][b]:
        a -= 1
    elif DP[a][b] == DP[a][b - 1]:
        b -= 1
    else:
        result.append(str2[a - 1])
        a -= 1
        b -= 1

result.reverse()
print(DP[-1][-1])
if DP[-1][-1]:
    print(''.join(result))