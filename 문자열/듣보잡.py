# 1764번 듣보잡
'''
김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 
듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.

첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다. 
이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과, 
N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다. 
이름은 띄어쓰기 없이 알파벳 소문자로만 이루어지며, 
그 길이는 20 이하이다. N, M은 500,000 이하의 자연수이다.

3 4
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhenrie
clinton



2
baesangwook
ohhenrie
'''

import sys

N, M = map(int,input().split())
dic = {}
for _ in range(N):
    per = sys.stdin.readline().strip()
    dic[per] = 1

cnt = 0
result = []

for _ in range(M):
    per = sys.stdin.readline().strip()
    if dic.get(per):
        cnt += 1
        result.append(per)

result.sort()
print(cnt)
if cnt:
    for name in result:
        print(name)
        
