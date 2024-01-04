# SWEA 4865  글자수

## 딕셔너리 이용

T = int(input())

for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    str_dic = {}
    for i in range(len(str1)):
        str_dic[str1[i]] = 0

    for j in range(len(str2)):
        try:                    # 문자열2에만 있는 경우엔 에러가 나므로 , 있는거만 추가해주기 위해 try 사용
            str_dic[str2[j]] += 1
        except:
            pass
    
    max = 0
    for value in str_dic.values():
        if value >= max:
            max = value
    
    print(f'#{tc} {max}')
