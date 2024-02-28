# 백준 1049번 기타줄
'''
기타에서 N개의 줄이 끊어졌다. 따라서 새로운 줄을 사거나 교체해야 한다. 
강토는 되도록이면 돈을 적게 쓰려고 한다. 
6줄 패키지를 살 수도 있고, 1개 또는 그 이상의 줄을 낱개로 살 수도 있다.
끊어진 기타줄의 개수 N과 기타줄 브랜드 M개가 주어지고, 각각의 브랜드에서 
파는 기타줄 6개가 들어있는 패키지의 가격, 낱개로 살 때의 가격이 주어질 때, 
적어도 N개를 사기 위해 필요한 돈의 수를 최소로 하는 프로그램을 작성하시오.

[입력]
4 2
12 3
15 4

[출력]
12
'''

N, M = map(int,input().split())
p6 = []     # 6개씩 살 때의 가격들
p1 = []     # 1개씩 살 때의 가격들
for _ in range(M):
    a, b = map(int,input().split())
    p6.append(a)
    p1.append(b)

min6 = min(p6)      # 6개 살때의 최소값
min1 = min(p1)      # 1개 살때의 최소값

if min1 * 6 <= min6:
    print(min1 * N)
else:
    a, b = divmod(N, 6)
    if min1 * b > min6:
        print(min6 * (a + 1))
    else:
        print(a * min6 + b * min1)
