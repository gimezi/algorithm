# 분수 찾기
# 각 단계 별로 마지막수
levels = [(i * (i + 1)) // 2 for i in range(1, 10000)]
goal = int(input())
for i in range(1, 9999):
    if goal == 1:
        print('1/1')
        break
    # 원하는 단계 찾기
    if levels[i - 1] < goal <= levels[i]:   
        target_level = i + 1
        target_num = goal - levels[i-1]
        if target_level % 2:
            n1 = target_level - target_num + 1
            n2 = target_num
            print(f'{n1}/{n2}')
            break
        else:
            n2 = target_level - target_num + 1
            n1 = target_num
            print(f'{n1}/{n2}')
            break


## 일일히 찾는 방법 -> 시간 초과남
# [
#     [(1, 1)],
#     [(1, 2), (2, 1)],
#     [(3, 1), (2, 2), (1, 3)],
#     [(1, 4), (2, 3), (3, 2), (4, 1)]
#     ...
# ]
# goal = int(input())

# # 피라미드 층수
# level = 1
# # 지금까지 몇개 했는지
# cnt = 0
# while True:
#     for num in range(level):
#         # 홀수 단계일 때
#         if level % 2:
#             temp = (level - num, num + 1)
#             cnt += 1
#             if cnt == goal:
#                 print(f'{temp[0]}/{temp[1]}')
#                 exit()
#         else: 
#             temp = (num + 1, level - num)
#             cnt += 1
#             if cnt == goal:
#                 print(f'{temp[0]}/{temp[1]}')
#                 exit()
#     level += 1
