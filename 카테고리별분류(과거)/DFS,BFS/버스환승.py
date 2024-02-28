# 1번: 방향배열(차르붐바) 
# 2번: 큐(계산기) / 과목평가랑 거의 비슷하게

# 버스 환승

from collections import deque

m, n = map(int,input().split())
k = int(input())
bus = {}
for _ in range(k):
    b, x1, y1, x2, y2 = map(int,input().split())   
    bus[b] = []
    if x1 == x2:
        for y in range(y1, y2 + 1):
            bus[b].append((x1, y))
    elif y1 == y2:
        for x in range(x1, x2 + 1):
            bus[b].append((x,y1))
sx, sy, dx, dy = map(int,input().split())

def BFS(start, end):
    que = deque([])
    for bus_num, bus_stop in bus.items():
        if start in bus_stop:
            que.append((bus_num, start, '' + str(bus_num)))
    visited = set()

    while que:
        num, loca, path = que.popleft()
        if end in bus[num]:
            return len(path)
        if loca not in visited:  # 들린 지점이 아니라면
            for i in bus[bus_num]:
                visited.add(i)
            for stops in bus[num]:
                for key, val in bus.items():
                    if stops in val and path.find(str(key)) == -1:
                        que.append((key, stops, path + str(key)))
                    

print(BFS((sx, sy),(dx, dy)))