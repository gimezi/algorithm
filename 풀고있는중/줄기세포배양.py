# SWEA A형대비: 줄기세포배양

'''
생명력이 x면, x초 뒤에 활성화 → 번식 가능
상하좌우로 번식
K시간 후 살아있는게 몇마리인지?

이건 배양용기를 어케 처리를 해야하나....
정보를 그리고 죽었는지, 활성인지, 비활성인지도 저장해줘야 한다...........


우선 MAP의 크기의 최대값은 max(N, M) + K * 2 임
'''
import copy
import pprint 

dir1 = [(1, 0), (0, 1), (-1, 0), (0, -1) ]
dir2 = []

N, M, K = map(int,input().split())
# 임시로 최대크기의 MAP을 만들어준다
maxlength = max(N, M) + 2 * K
# maxlength = 15
MAP = [[0 for _ in range(maxlength)] for _ in range(maxlength)]
mid = maxlength // 2
# 값을 중앙에 놓으려면 시작 점이... 
for i in range(N):
    i += mid - N//2
    arr = list(map(int,input().split()))
    for j in range(M):
        start = mid - M//2
        if arr[j]:
            MAP[i][start + j] = (arr[j], 1, 0)  # 크기, (죽음 : 0, 비활성: 1, 활성: 2), 0초

# MAP을 그냥 계속 업데이트 해주자...
time = 0
while time < K:
    # pprint.pprint(MAP)
    NOWMAP = copy.deepcopy(MAP)
    # 겹칠때 큰걸 넣어주기 위해
    changelst = [[0 for _ in range(maxlength)] for _ in range(maxlength)]
    for i in range(maxlength):
        for j in range(maxlength):
            if MAP[i][j]:
                flag = True
                x, state, second = MAP[i][j]
                # 비활성이라면
                if state == 1:
                    # 만약 비활성인데 시간을 다채웠다면
                    if second == x:
                        state = 2
                        second = 0
                    else:
                        second += 1
                if state == 2:
                    if second == 0:
                        for dy, dx in dir1:
                            ny, nx = i + dy, j + dx
                            # 인접한데 비어있다면
                            if MAP[ny][nx] == 0:
                                # 만약에 겹친다면
                                if changelst[ny][nx]:
                                    # 내가 더 크다면
                                    if changelst[ny][nx] < x:
                                        NOWMAP[ny][nx] = (x, 1, 0)
                                        changelst[i][j] = x
                                else:
                                    NOWMAP[ny][nx] = (x, 1, 0)
                        second += 1            
                    if second == x:
                        state = 0   # 죽음
                        second = 0
                NOWMAP[i][j] = (x, state, second)
    MAP = NOWMAP
    time += 1

cnt = 0

pprint.pprint(MAP)
for i in range(maxlength):
    for j in range(maxlength):
        if MAP[i][j]:
            if MAP[i][j][1] == 1:
                cnt += 1
            elif MAP[i][j][1] == 2:
                cnt += 1

print(cnt)
                
