# 백준 11725번 트리의 부모 찾기

'''
루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 
각 노드의 부모를 구하는 프로그램을 작성하시오.
첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 
둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

[입력]
7
1 6
6 3
3 5
4 1
2 4
4 7

[출력]
4
6
1
3
1
4

'''

'''
BFS를 하자
'''
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

def find(start):
    result = [0 for _ in range(N + 1)]
    que = deque([start])
    while que:
        past = que.popleft()
        for i in arr[past]:
            if not result[i]:
                result[i] = past
                que.append(i)
    return result

ans = find(1)
for i in range(2, N + 1):
    print(ans[i])

    
  

