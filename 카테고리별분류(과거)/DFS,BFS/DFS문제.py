# DFS시작하기
'''
트리 DFS를 돌리려합니다
숫자 n과 인접행렬을 입력받습니다
DFS를 돌리고, 탐색 순서대로 출력해주세요

[유의사항]
1. 노드값은 없으며, 노드번호를 출력하시면 됩니다
2. 항상 0번부터 탐색을 시작합니다
3. 자식 노드가 여러개라면, 노드번호가 작은 것부터 탐색합니다
4. 1<= n <= 100
5. 노드이 번호는 0 ~ n-1번까지 있습니다

[input]
5
0 1 1 0 0
0 0 0 1 1 
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0

[output]
0 1 3 4 2
'''

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * (N + 1)


def DFS(n,arr):
    global visited
    stack = []
    visited[n] = 1
    lst =[]
    lst.append(n)
  
    while True:
        for m in range(N):
            if arr[n][m] == 1 and visited[m] == 0:
                stack.append(n)
                visited[m] = 1
                lst.append(m)
                n = m
                break
        else:
            if stack:
                n = stack.pop()
            else:
                break

    return lst

    
print(*DFS(0,arr))