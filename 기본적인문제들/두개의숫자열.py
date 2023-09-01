# 두개의 숫자열
# 테스트의 갯수 받아오기
test = int(input())
 
for test_num in range(1,test+1):
    #a랑 b 값 받아오기
    a_num, b_num = map(int, input().split())
    a = map(int,input().split())
    a = list(a)
    b = map(int,input().split())
    b = list(b)
    s = []
     
    #밀어서 계산하기
 
    if a_num >= b_num:  # a개수가 더 많을 때
 
        dif1 = a_num - b_num #둘의 갯수차이
 
        for k in range(dif1+1):
            S1 = 0
            for i in range(b_num):
                p = a[i+k] * b[i]
                S1 = S1 + p
            s.append(S1)
     
    else: #b가 더 많을때
 
        dif2 = b_num - a_num  #둘의 갯수차이
 
        for k in range(dif2+1):
            S2 = 0
            for i in range(a_num):
                p = a[i] * b[i+k]
                S2 = S2 + p
            s.append(S2)
 
    ans = max(s)
     
    #최대값 출력
    print("#{} {}".format(test_num,ans))