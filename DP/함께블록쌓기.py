# 백준 18427번 함께 블록 쌓기
'''
1번부터 N번까지의 학생들은 각각 블록을 갖고 있음
인당 최대 M개의 블록을 가지고 잇고, 각 학생이 갖고 있는 블록의 높이는 다 다름

학생들이 번호 순서대로 블록을 사용해서 하나틔 탑을 만들려고 한다
어떤 학생은 블록을 안써도 되고, 한 학생 당 최대 1개의 블록을 사용할 수 있다.

각 학생이 가지고 있는 블록에 대한 정보가 주어졌을 때
높이가 정확히 H인 탑을 만들 수 있는 경우의 수를 계산하세요

'''

N, M, H = map(int, input().split())
students = [list(map(int, input().split())) for _ in range(N)]
# 각각의 dp[5] = 5를 만드는 경우의 수
dp = [0 for _ in range(H + 1)]

# 누적합 구하기
# 첫번째 학생부터
for student in students:
    # 중복을 없애기 위해서 뒤에서부터 봤을 때
    for i in range(H,0,-1):
        # 만약에 dp가 0이면 = 아직 못 만듬 pass
        if dp[i] == 0:
            continue
        # 학생이 가지고 있는 박스에 대해서
        for box in student:
            # 만약 해당 숫자랑 지금 박스랑 더한게 H보다 크다면 넘겨주고
            if i + box > H:
                continue
            # 아니라면 해당 숫자 + 박스에 앞의 경우의 수를 더해주자
            dp[i+box] += dp[i]
    # 그리고 각각의 숫자는 하나의 경우의 수이므로 1을 더해주자
    for box in student:
        dp[box] += 1
print(dp[H]%10007)