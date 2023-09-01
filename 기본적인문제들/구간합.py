# 4835 구간합

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int,input().split())
    nums = list(map(int,input().split()))

    sums = []
    for i in range(N - M + 1):
        sum_of_arr = 0
        for j in range(M):
            sum_of_arr += nums[i + j]
        sums.append(sum_of_arr)
    
    max_sum = max(sums)
    min_sum = min(sums)
    print(f'#{tc} {max_sum - min_sum}')



# # 강사님 코드(비슷하게 푼듯?)

# T = int(input())

# for tc in range(1, T + 1):
#     N, M = map(int,input().split())
#     nums = list(map(int,input().split()))
#     new_nums = []

#     for i in range(N - M + 1):
#         result = 0 
#         for j in range(i, i + M):
#             result += nums[j]
#         new_nums.append(result)

#     print(f'#{tc} {max(new_nums) - min(new_nums)}')
    


