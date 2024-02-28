# 4834 숫자카드

# T = int(input())

# for tc in range(1, T + 1):
#     N = int(input())
#     nums = list(map(int,input()))
    
#     # 개수를 세어보자
#     count = [0] * (max(nums) + 1)
#     for num in nums:
#         count[num] += 1
#     max_count = 0
#     for i in range(len(count)):
#         if count[max_count] <= count[i]:
#             max_count = i

#     print(f'#{tc} {max_count} {count[max_count]}')


# 강사님 코드

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    cards = input()
    counts = {str(n) : 0 for n in range(10)}
    # 각 숫자의 등장 횟수를 세기
    for card in cards:
        counts[card] += 1
    max_count = max(counts.values())
   # max_count와 같은 횟수를 가진 숫자들 중 가장 큰 숫자를 찾는다.
   #  
    max_number = max([int(num) for num, count in counts.items() if count == max_count])

    print(f'#{tc} {max_number} {max_count}')