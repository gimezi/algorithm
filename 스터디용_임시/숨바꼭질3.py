# 13549번 숨바꼭질 3

'''
수빈이는 동생과 숨바꼭질을 하고 있다. 
수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 
동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 
수빈이는 걷거나 순간이동을 할 수 있다. 
만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 
수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 
구하는 프로그램을 작성하시오.

[입력]
5 17

[출력]
2
'''
'''
순간이동이면 0초임!!!!

[데이크스트라]
그래프에서 꼭짓점 간의 최단 경로를 찾는 알고리즘
약간 DP + BFS

https://velog.io/@zirryo/Algorithm-%EB%8D%B0%EC%9D%B4%ED%81%AC%EC%8A%A4%ED%8A%B8%EB%9D%BC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98
'''
from collections import deque

N, K = map(int, input().split())

def find(n, k):
    que = deque([n, 0])

    while que:
        now, s = que.popleft()
        que.append(2 * now)
