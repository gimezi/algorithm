# 4837 부분집합의 합


def subset_sum(arr, n, sums):
    length = len(arr)
    count = 0
    for i in range(1 << length):
        subset = []
        for j in range(length):
            if i & (1 << j):
                subset.append(arr[j])
        
        if len(subset) == n and sum(subset) == sums:
            count += 1
    
    return count


arr = list(range(1, 13))

T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    print(f'#{tc + 1} {subset_sum(arr, n, m)}')

    
# for i in range(1<<12):
#     sub = []
#     for j in range(12):
#         if i & (1<<j):
#             sub.append(arr[j])
#     if len(sub) == 2:
#         print(sub)