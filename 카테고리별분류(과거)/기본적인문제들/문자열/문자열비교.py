# SWEA 문자열 비교

T = int(input())

for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    for j in range(len(str2) - len(str1) + 1):
        a = 0
        for i in range(len(str1)):
            if str1[i] == str2[i + j]:
                a += 1
        
        if a == len(str1):
            result = 1
            break
        else:
            result = 0
    print(f'#{tc} {result}')

