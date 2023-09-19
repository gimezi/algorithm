'''
도깨비의 보자기에는 n개 황금이 들어있습니다.
이 보자기는 한번 꺼낼 때가장 가벼운 물건만 꺼내지는마법의 보자기입니다.
보자기에 있는 황금을 꺼내면 보자기의 무게는 점점 가벼워집니다.
도깨비에게 들키지 않도록, 황금을 2개씩 꺼낼 때 마다 
무거운 짱돌 1개를 넣어두려고 합니다.

황금의 개수 n과
보자기에 들어있는 황금의 무게들을 입력 받습니다.
보자기에서 2 개의 내용물을 꺼냅니다.
그리고 마지막으로 꺼낸 황금의 2 배 무게를 가진 짱돌 1개 넣습니다.
꺼내어진 돌이 황금이 아닐 때까지위 동작을 반복 합니다.

5
1 3 3 4 9

4
'''
from heapq import heapify, heappop, heappush
import copy

n = int(input())
bojagi = list(map(int,input().split()))
gold = copy.deepcopy(bojagi)
heapify(bojagi)
dol = []
cnt = 0
while True:
    a = heappop(bojagi)
    if a in dol:
        break
    cnt += 1
    b = heappop(bojagi)
    if b in dol:
        break
    cnt += 1
    c = b * 2
    dol.append(c)
    heappush(bojagi, c)

check = heappop(bojagi)
if check == a or check == b:
    cnt += 1
print(cnt)