# SWEA 최소 신장트리

# Union-Find 심화
'''
그래프에서 사이클을 제거하고 모든 노드를 포함하는 트리를 구성할 때,
가중치의 합이 최소가 되도록 만든 경우를 최소신장트리라고 한다.
0번부터 V번까지의 노드와 E개의 간선을 가진 그래프 정보가 주어질 때
이 그래프로부터 최소신장트리를 구성하는 간선의 가중치를 
모두 더해 출력하는 프로그램을 만드세요

'''
'''
T = int(input())
for tc in range(1, T + 1):
    V, E = map(int,input().split())
    edge = []
    for _ in range(E):
        f, t, w = map(int,input().split())
        edge.append([f, t, w])

    # w를 기준으로 정렬
    edge.sort(key=lambda x:x[2])

    # 사이클이 발생하는지 확인하기 -> Union Find
    parents = [i for i in range(V + 1)]

    def find_set(x):
        if parents[x] == x:
            return x
        
        parents[x] = find_set(parents[x])
        return parents[x]

    def union(x, y):
        x = find_set(x)
        y = find_set(y)

        if x == y:
            print('사이클발생')
            return
        
        if x < y:
            parents[y] = x
        else:
            parents[x] = y

    cnt = 0
    sum_weight = 0
    for f, t, w in edge:
        # 사이클이 발생하지 않는다면
        if find_set(f) != find_set(t):
            cnt += 1
            union(f, t)
            sum_weight += w
            # MST 구성이 끝나면
            if cnt == V:
                break

    print(f'#{tc} {sum_weight}')
'''


# 강사님 코드

def find(node):
    if parents[node] != node:
        parents[node] = find(parents[node])
    return parents[node]

def union(a, b):
    pa = find(a)
    pb = find(b)
    if pa < pb:
        parents[pb] = parents[pa]
    else:
        parents[pa] = parents[pb]
    
T = int(input())
for tc in range(1, T + 1):
    v,e = map(int,input().split())
    # 받으면서 바로 정렬
    edges = sorted([list(map(int,input().split())) for _ in range(e)], key=lambda x:x[2])
    parents = [i for i in range(v + 1)]
    totalv = 0
    cnt = 0
    
    for i in range(e):
        if cnt == v:
            break
        s, e, w = edges[i]
        if find(s) == find(e):  # 시작 노드와 끝 노드의 부모가 같으면 continue
            continue
        union(s, e)
        totalv += w
    print(f'#{tc} {totalv}')







