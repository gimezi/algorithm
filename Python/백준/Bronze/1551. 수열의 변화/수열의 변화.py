# 수열의 변화

N, K = map(int,input().split())
arr = list(map(int,input().split(',')))
# 몇번했는지 체크할 cnt
cnt = 0
while cnt < K:
    # 다음에 계산할 arr
    next_arr = [0 for _ in range(len(arr) - 1)]
    for i in range(len(arr) - 1):
        next_arr[i] = arr[i + 1] - arr[i]
    cnt += 1
    arr = next_arr

ans = ''
for num in arr:
    ans += str(num)
    ans += ','

print(ans[:-1])