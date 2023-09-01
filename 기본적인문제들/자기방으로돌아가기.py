# 4408 자기 방으로 돌아가기
'''
각자 현재 방에서 돌아갈 방으로 가야하는데 길이 겹치면 안됨
홀수방이 위에있고 짝수방이 아래에 있음
테케 수
돌아가야 할 학생들의 수
현재 방. 돌아갈 방


3 
4 
10 20   
30 40
50 60
70 80
2 
1 3
2 200
3
10 100
20 80
30 50


#1 1
#2 2
#3 3	// Test Case 1의 정답
// Test Case 2의 정답
// Test Case 3의 정답

비슷한 문제: 삼성시의 버스 노선
'''


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    bang = [0 for _ in range(201)]  # 1부터 200번까지 쓸꺼임
    for i in range(N):
        now, goal = map(int,input().split())
        now = (now + now % 2) // 2
        goal = (goal + goal % 2) // 2
        for j in range(min(now, goal), max(now, goal) + 1):
            bang[j] += 1
    print(f'#{tc} {max(bang)}')

## min과 max를 적극 활용하자
## 방번호가 어케 바뀔지 미리 식을 세워두고 하자
