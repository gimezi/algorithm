# 백준 2138번 전구와 스위치

'''
N개의 스위치와 N개의 전구가 있다. 각각의 전구는 켜져 있는 상태와 꺼져 있는 상태 중 하나의 상태를 가진다. 
i(1 < i < N)번 스위치를 누르면 i-1, i, i+1의 세 개의 전구의 상태가 바뀐다. 즉, 꺼져 있는 전구는 켜지고, 켜져 있는 전구는 꺼지게 된다. 
1번 스위치를 눌렀을 경우에는 1, 2번 전구의 상태가 바뀌고, N번 스위치를 눌렀을 경우에는 N-1, N번 전구의 상태가 바뀐다.
N개의 전구들의 현재 상태와 우리가 만들고자 하는 상태가 주어졌을 때, 
그 상태를 만들기 위해 스위치를 최소 몇 번 누르면 되는지 알아내는 프로그램을 작성하시오.
'''
'''
그냥 앞에서 부터 쭈루루루룩하면 된다
'''

import copy
N = int(input())
start = list(map(int,input()))
goal = list(map(int,input()))


def click(switch, cnt):
    for i in range(1, N):
        # 앞에 꺼가 목표와 다르면 눌러주고
        if switch[i-1] != goal[i-1]:
            cnt += 1
            switch[i - 1] = 1 - switch[i - 1]
            switch[i] = 1 - switch[i]
            if i != N - 1:
                switch[i + 1] = 1 - switch[i + 1]
    if switch[-1] != goal[-1]:
        return -1
    else:
        return cnt

result1 = click(start, 0)
start2 = copy.deepcopy(start)
start2[0] = 1 - start2[0]
start2[1] = 1 - start2[1]
result2 = click(start2, 1)
if result1 != -1:
    print(result1)
elif result2 != -1:
    print(result2)
else:
    print(-1)
