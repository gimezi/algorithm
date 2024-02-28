# 백준 텀 프로젝트
'''
DFS?


2
7
3 1 3 7 3 4 6
8
1 2 3 4 5 6 7 8
'''

def dfs(start):
    stack = [(start, [start])]
    while stack:
        now, group = stack.pop()
        next = students[now -1]
        print(next)
        group.append(next)
        if next == start:
            for num in group:
                visited[num] = 0
            break
        stack.append((next, group))

n = int(input())
students = list(map(int,input().split()))
visited = [1 for _ in range(n)]
for i in range(n):
    if visited[i] == 1:
        dfs(i + 1)
print(visited)


