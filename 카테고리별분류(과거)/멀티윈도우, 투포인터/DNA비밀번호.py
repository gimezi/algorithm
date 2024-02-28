# 12891번 DNA 비밀번호

'''
[입력]
첫 번째 줄에 민호가 임의로 만든 DNA 문자열 길이 |S|와 
비밀번호로 사용할 부분문자열의 길이 |P| 가 주어진다. (1 ≤ |P| ≤ |S| ≤ 1,000,000)
두번 째 줄에는 민호가 임의로 만든 DNA 문자열이 주어진다.
세번 째 줄에는 부분문자열에 포함되어야 할 {A, C, G, T} 의 최소 개수가 공백을 구분으로 주어진다.
각각의 수는 |S| 보다 작거나 같은 음이 아닌 정수이며 총 합은 |S| 보다 작거나 같음이 보장된다.
9 8
CCTGGATTG
2 0 1 1

[출력]
첫 번째 줄에 민호가 만들 수 있는 비밀번호의 종류의 수를 출력해라.
0
'''
def check():
    cnt = 0
    for val in cntdic.values():
        cnt += val
    if cnt:
        return 0
    else:
        return 1

S, P = map(int,input().split())
ori_str = input() * 2
limit = list(map(int,input().split()))
ans = 0
mystr = ori_str[:P]
cntdic = {'A': limit[0], 'C' : limit[1],  'G' : limit[2], 'T': limit[3]}
for i in mystr:
    cntdic[i] -= 1
    if cntdic[i] < 0:
        cntdic[i] = 0
if check():
    ans += 1

for l in range(S):
    if cntdic[ori_str[l]]:
        cntdic[ori_str[l]] += 1
    if not cntdic[ori_str[l + P]]:
        cntdic[ori_str[l + P]] -= 1
    print(ori_str[l], ori_str[l + P])
    print(cntdic)
    if check():
        ans += 1
print(ans)
