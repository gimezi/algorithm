# 범인의 흔적
'''
추적을 시작할 index를 입력받으세요
5번 인덱스를 보면 범인은 4번에서 출발하고 9시에 도착함
4번을 보면 2번으로 가고 8시에 도착함
2번을 보면 0번인덱스와 5시를 알수 잇다
-1 에서 잡을 수 있을때 0번부터 어느 인덱스로 갔는지 순서대로 출력하세요

evid = [-1, 0, 0, 1, 2, 4, 4]
timestamp = [8, 3, 5, 6, 8, 9, 10]

[input]
추적을 시작할 인덱스
5

[output]
0번index(출발)
2번index(5시)
4번index(8시)
5번index(9시)
'''


# evid = [-1, 0, 0, 1, 2, 4, 4]
# timestamp = [8, 3, 5, 6, 8, 9, 10]

# N = int(input())

# def DFS(idx, time):
#     if evid[idx] == -1:
#         print(f'{idx}번index(출발)')
#         return
    
#     DFS(evid[idx], timestamp[idx])
#     print(f'{idx}번index({timestamp[idx]}시)')

# DFS(N, timestamp[N])














start = int(input())

evid = [-1, 0, 0, 1, 2, 4, 4]
timestamp = [8, 3, 5, 6, 8, 9, 10]

def find(n):
    if evid[n] == -1:
        print(f'{n}번index(출발)')
        return 
    
    print(f'{n}번index({timestamp[n]}시)')
    return find(evid[n])

find(start)