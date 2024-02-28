# 백준 13144번
'''
시간 초과
반례

5
1 2 2 2 1

7
'''

N = int(input())
arr = list(map(int,input().split()))
maxnum = max(arr)
ans = 0
p1, p2 = 0, 0
check = [False] * 100001
while p1 != N:
    if p1 == p2 or check[arr[p2]] == False:
        check[arr[p2]] = True
        ans += 1
        p2 += 1
        if p2 == N:
            p1 += 1
            check = [False] * 100001
            p2 = p1
    else:
        p1 += 1
        check = [False] * 100001
        p2 = p1

print(ans)
