# 답안지 채점

'''
정답을 맞춘 문제는 1점이 주어진다.
연속으로 정답을 맞출 경우, 이 전 점수에서 보너스 1점이 가산되어 주어진다.
M개의 문제에 대한 N명의 학생들의 답안지가 입력으로 주어졌을 때, 
가장 높은 점수를 받은 학생과, 가장 낮은 점수를 받은 학생의 점수차를 출력하는 프로그램을 작성하라.

[input]
4
5 10
5 5 5 1 5 3 3 3 3 4
4 2 1 3 1 2 1 4 3 4
2 5 5 1 5 3 3 3 3 4
1 5 5 3 2 3 3 3 5 5
4 5 5 1 5 3 5 4 3 4
5 5 5 2 4 1 3 1 5 1
6 22
2 3 1 4 5 4 3 1 3 3 1 2 3 4 1 3 4 2 2 4 1 5
5 2 5 1 1 2 3 2 3 2 5 1 3 4 1 3 2 3 2 5 4 1 
5 3 1 4 5 4 3 1 3 3 1 2 3 4 1 3 4 2 2 4 1 5
5 4 2 3 5 5 4 3 3 3 4 3 1 1 3 3 5 3 1 4 5 3
4 2 5 1 2 5 2 2 3 5 2 5 3 4 5 2 4 2 1 1 4 5
5 3 4 3 3 5 1 3 5 2 1 5 2 3 2 2 4 3 4 5 1 1
1 5 5 4 5 2 2 4 4 2 2 3 4 1 1 4 1 4 4 4 1 3
6 6
1 4 4 1 1 5
3 4 2 1 4 2
5 2 5 3 5 3
1 1 4 1 1 5
1 1 4 1 1 5
4 5 4 3 2 5
4 3 5 2 5 3
7 13
5 5 3 3 5 5 2 3 2 4 2 4 2 
4 1 3 3 5 5 2 3 2 4 2 4 2
1 5 3 4 5 3 5 2 5 5 5 4 2
5 1 3 3 5 5 2 3 2 4 2 4 2 
3 2 5 1 4 2 5 4 5 4 5 2 2 
4 2 5 4 4 2 2 4 1 3 1 3 4 
2 4 5 4 3 1 4 4 2 4 3 2 3
1 3 1 5 1 2 3 1 2 1 2 3 5

[output]
#1 42
#2 227
#3 11
#4 66
'''

def grade(ans, stu):
    bonus = 0
    score = 0
    for i in range(M):
        if ans[i] == stu[i]:
            score += 1
            score += bonus
            bonus += 1
        else:
            bonus = 0
    return score

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int,input().split())
    answer = list(map(int, input().split()))
    student = [list(map(int, input().split())) for _ in range(N)]

    max_score = 0
    min_score = 100000
    for j in range(N):
        sscore = grade(answer, student[j])
        if sscore <= min_score:
            min_score = sscore
        if sscore >= max_score:
            max_score = sscore

    result = max_score - min_score

    print(f'#{tc} {result}')