# 간단한 소인수분해 SWEA

'''
N=2^a x 3^b x 5^c x 7^d x 11^e
'''


def cal(N):
    for i in range(5):
        if N % nums[i] == 0:
            ans[i] += 1
            N //= nums[i]
    if N > 1:
        cal(N)
    else:
        return

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    ans = [0, 0, 0, 0, 0]
    nums = [2, 3, 5, 7, 11]
    cal(N)
    print(f'#{tc}',*ans)
