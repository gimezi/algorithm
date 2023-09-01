# 인디언 합창단
'''
총 26명

'''

def find(node):
    if node != root[node]:
        root[node] = find(root[node])
    return root[node]
    

def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x == root_y:    # 이미 같은 팀인 경우 명령무시
        return

    if rank[root_x] > rank[root_y]:
        root[root_y] = root_x
    else:
        root[root_x] = root_y
        if rank[root_x] == rank[root_y]:
            rank[root_y] += 1

rank = [0] * 26
root = [i for i in range(26)]
for _ in range(int(input())):
    p1, p2 = input().split()
    p1 = int(ord(p1)) - 65
    p2 = int(ord(p2)) - 65
    union(p1, p2)
  
for i in range(26):
    find(i)

DAT = [0] * 26
team = 0

for i in range(26):
    DAT[root[i]] += 1

indi = 0
for data in DAT:
    if data > 1:
        team += 1
    elif data == 1:
        indi += 1

print(team)
print(indi)