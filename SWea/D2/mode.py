# 최빈수 구하기
n = int(input())
 
for p in range(1,n+1):
    num = int(input())
 
    #빈 딕셔너리 생성
    dic = {}
 
    # input값을 딕셔너리에 저장
    data = map(int,input().split())
    data = list(data)
    for i in range(0,101):
        dic[i] = 0
        for j in data:
            if j == i:
                dic[i] += 1
    #print(dic)
 
    # 딕셔너리에서 최빈값을 구하는 함수
    pos = []
     
    for value, count in dic.items():
        if count == max(dic.values()):
            #print(value)
            pos.append(value)
 
    itsme = max(pos)
 
    print("#{} {}".format(num,itsme))