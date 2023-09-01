# 수학 놀이
'''
+1을 할때에, 끝에다가 1을 붙이는 식으로 계산을 하고 있다.
A, B가 있을때, A에서 x2 또는 +1 연산을 했을때 해당 숫자를 만들 수 있는가?
2 x 2 = 4
4 x 2 = 8
8 x 2 = 16
16 + 1 = 161
161 x 2 = 322


[입력]
2 322

[출력]
5
안된다면 -1
'''
from collections import deque

A, B = map(int, input().split())

def BFS(n, goal):
    que = deque([(n, 0)])
    while que:
        now, level = que.popleft()
        if now == goal:
            return level
        else:
            a = now * 2
            b = now * 10 + 1
            if a <= goal:
                que.append((a, level + 1))
            if b <= goal:
                que.append((b, level + 1))
    return -1

print(BFS(A, B))

'''
a, b = map(int,input().split())
cnt = 0
while b >= a:
    if b == a:
        print(cnt)
        exit()
    if b % 10 == 1:     # 1의 자리가 1인 경우, 1을 제거
        b //= 10
    elif b % 2 == 0:    # 짝수인 경우 2로 나눈다
        b //= 2
    else:               # 두 조건이 모두 해당하지 않으면, b를 a로 만들 수 없다. 
        print(-1)
        exit()
    cnt += 1
print(-1)
'''


