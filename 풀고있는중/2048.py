# 백준 12100번 2048
'''
1. 기존 게임과 다르게 블럭 추가 안됨
2. 한번만 합쳐질 수 있음
3. 만약 3개 이상이 합쳐질 수 있다면, 움직이려는 방향에 있는 애들이 합쳐짐

최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값은?

[How?]
→ 보드판이 최대 20 * 20
한번 합쳐지면 더 안됨, 그럼 합쳐진건지에 대한 체크용이 필요함
이게 한번 합쳐지면 다시 안되므로
우선 가장 크게 나올수 있는 경우가
제일 큰 수가 2개있다면 → 그게 합쳐질 수 있다면 제일 큰수,.
아니라면, 그 다음꺼 찾고 등등.. 이렇게 해보면 될것같음

숫자가 2보다 크거나 같고 2의 제곱꼴임
'''
import copy

N = int(input())
board = [[] for _ in range(N)]
maxnum = 0
for i in range(N):
    arr = list(map(int,input().split()))
    for num in arr:
        board[i].append((num, 0))
    if maxnum < max(arr):
        maxnum = max(arr)


# 위로 밀기
def up(board):
    newboard = [[(0, 0) for _ in range(N)]for _ in range(N)]
    for j in range(N):
        nowidx = 0
        nextidx = 1
        idx = 0 #여기서부터 채워요
        while nextidx <= N:
            # 비교하는 애가 0이라면 뒤로 
            if board[nowidx][j][0] == 0:
                nowidx += 1        
                nextidx += 1
            else:
                if nextidx != N:
                    now = board[nowidx][j]
                    next = board[nextidx][j]
                    # 서로 같고 합쳐지지 않았다면
                    if now[0] == next[0] and now[1] == 0 and next[1] == 0:
                        nowidx += 2
                        nextidx += 2
                        newboard[idx][j] = (now[0] * 2, 1)
                        idx += 1
                    # 앞에 꺼는 있는데 뒤에가 0이라면
                    elif next[0] == 0:
                        nextidx += 1
                    # 안합쳐진다면
                    else:
                        newboard[idx][j] = (now[0], 0)
                        idx += 1
                        nowidx += 1
                        nextidx += 1
    
    return newboard

print(up(board))
                



# board = [[(2, 0), (2, 0), (2, 0)], [(4, 0), (4, 0), (4, 0)], [(8, 0), (8, 0), (8, 0)]]
def game(nowboard, level, nowmax):
    # 종료조건 1. 5번 다 돌았을 때
    if level == 5:
        return
    # 종료조건 2. 이미 최대치를 찍었을 때 = 제일 큰 수의 두배
    if nowmax == 2 * maxnum:
        return
    
    # 위로 밀어보자
    nextboard = copy.deepcopy(nowboard)