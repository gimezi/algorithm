## 1107 리모컨
'''
수빈이는 TV를 보고 있다. 수빈이는 채널을 돌리려고 했지만, 
버튼을 너무 세게 누르는 바람에, 일부 숫자 버튼이 고장났다.
리모컨에는 버튼이 0부터 9까지 숫자, +와 -가 있다. 
+를 누르면 현재 보고있는 채널에서 +1된 채널로 이동하고, 
-를 누르면 -1된 채널로 이동한다. 
채널 0에서 -를 누른 경우에는 채널이 변하지 않고, 채널은 무한대 만큼 있다.
수빈이가 지금 이동하려고 하는 채널은 N이다. 어떤 버튼이 고장났는지 주어졌을 때, 
채널 N으로 이동하기 위해서 버튼을 최소 몇 번 눌러야하는지 구하는 프로그램을 작성하시오.
수빈이가 지금 보고 있는 채널은 100번이다


[입력]
5457
3
6 7 8

[출력]
6
'''

# 그냥 무식하게 다 비교하는게 빠를듯
N = int(input())        # 이동하려고 하는 채널
M = int(input())        # 고장난 버튼의 개수
now = 100               # 현재 채널
if M:   
    broken = list(map(int,input().split()))
    usable = []         # 쓸 수 있는 번호들
    for i in range(10):
        if i not in broken:
            usable.append(i)
else:
    usable = [i for i in range(0, 10)]


mincnt = abs(100 - N)

for i in range(1000000):
    num = str(i)
    for k in range(len(num)):
        if int(num[k]) not in usable:
            break
        if k == len(num) - 1:
            mincnt = min(mincnt, abs(N - i) + len(num))

print(mincnt)










































'''
# 시간초과남ㅓ
N = int(input())        # 이동하려고 하는 채널
M = int(input())        # 고장난 버튼의 개수
now = 100               # 현재 채널
if M:   
    broken = list(map(int,input().split()))
    usable = []         # 쓸 수 있는 번호들
    for i in range(10):
        if i not in broken:
            usable.append(i)
else:
    usable = [i for i in range(0, 10)]

def check(num):
    if num < 0:
        return 0
    num = list(str(num))
    div = list(map(int,num))
    for n in div:
        if n not in usable:
            return 0
    return 1


N1, N2, N3, N4 = N, N, 100, 100
cnt = 0

while True:
    N3 += 1
    N4 -= 1
    cnt += 1
    if N3 == N or N4 == N:
        break
    if N1 < 5000001:
        if check(N1):
            if check(N2):
                if len(str(N1)) > len(str(N2)):
                    cnt += len(str(N2)) - 1 
                    break
            cnt += len(str(N1)) - 1
            break
    
    if N2 > 0:
        if check(N2):
            cnt += len(str(N2)) - 1 
            break
    N1 += 1
    N2 -= 1
    
print(cnt)
'''