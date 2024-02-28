# 어디에 단어가 들어갈 수 있을까
'''
주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 
자리의 수를 출력하는 프로그램을 작성하라.

[입력]
첫 줄에는 테스트 케이스의 개수 T
가로,세로의 길이 N과 단어의 길이 K가 주어진다
퍼즐의 모양이 주어지고, 흰색은 1, 검은색은 0으로 주어진다.
10
5 3
0 0 1 1 1
1 1 1 1 0
0 0 1 0 0
0 1 1 1 1
1 1 1 0 1
5 3
1 0 0 1 0
1 1 0 1 1
1 0 1 1 1
0 1 1 0 1
0 1 1 1 0

[출력]
#1 2
#2 6
'''

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = [list(map(int,input().split())) for _ in range(N)]
    ans = 0
    
    # 가로로 찾기
    for arr in puzzle:
        cnt1 = 0
        for i in range(N):
            if arr[i]:
                cnt1 += 1
            if arr[i] == 0 or i == N - 1:
                if cnt1 == K:
                    ans += 1
                cnt1 = 0        
                        

    # 세로로 찾기
    for i in range(N):
        cnt2 = 0
        for j in range(N):
            if puzzle[j][i]:
                cnt2 += 1
            if puzzle[j][i] == 0 or j == N - 1:
                if cnt2 == K:
                    ans += 1
                cnt2 = 0
    
                
                
    print(f'#{tc} {ans}')