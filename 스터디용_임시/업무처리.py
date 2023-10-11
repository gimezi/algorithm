# A형 기출: 업무처리

# BFS로 풀어야하나..


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    is_true = True
    work = [list(map(int,input().split())) for _ in range(N)]
    DP = [[0, 0] for _ in range(N)]
    todolst = [[] for _ in range(N)]

    # 모두 계산되었는지 확인용
    check = [1 for _ in range(N)]

    for i in range(N):
        # 선행일이 없다면, 
        if work[i][1] == 0:
            check[i] = 0
            # 코코 도움 없음
            DP[i][0] = work[i][0]
            # 코코 도움 있음
            DP[i][1] = work[i][0] // 2
        # 선행일이 있다면, todolst에 저장
        else:
            for k in range(1, len(work[i])):
                todolst[i].append(work[i][k] - 1)

    # 모두가 선행일을 가지고 있음 -> 안댐
    if sum(check) == N:
        is_true = False

    while sum(check):
        update = False
        for i in range(N):
            breakpoint
            # 계산되지 않았다면
            if check[i]:
                flag = True
                time = [[],[]]
                for num in todolst[i]:
                    # 선행일이 계산이 안되었다면 넘기고
                    if DP[num][0] == 0:
                        flag = False
                        break
                    else:
                        time[0].append(DP[num][0])  # 코코 도움 없이
                        time[1].append(DP[num][1])  # 코코 도움 있음
                
                # 선행일이 모두 계산되었다면, 
                if flag:
                    update = True
                    # 우선 그냥 쌩으로 한다면 선행일 중에 긴거 + 지금꺼 시간
                    DP[i][0] = work[i][0] + max(time[0])

                    # 코코가 도와준다면,
                    maxtime = 0
                    for k in range(len(time[1])):
                        if time[1][k] > maxtime:
                            # 코코가 도와준 거 중에 제일 긴거
                            maxtime = time[1][k]
                            idx = k
                    temp = 0
                    # 도와준거 빼고는 원래 값
                    for j in range(len(time[1])):
                        if j == idx:
                            pass
                        else:
                            if time[0][j] > temp:
                                # 반 줄은거 뺴고 제일 긴거
                                temp = time[0][j]
                    # 이미 한번 도와줬다면
                    once = max(maxtime, temp) + work[i][0]
                    # 이번에 도와주는거랑 비교
                    DP[i][1] = min(once, max(time[0]) + (work[i][0] // 2))
                    check[i] = 0
        if not update:
            is_true = False
            break

    if is_true:
        result = 0 
        for i in range(N):
            if DP[i][1] > result:
                result = DP[i][1]
                idx = i
        for k in range(N):
            if k == idx:
                pass
            else:
                if DP[k][0] < result:
                    result = DP[k][0]
        print(f'#{tc} {result}')
    else:
        print(f'#{tc} -1')