# #1206번 View

T = 10

for j in range(T):
    N = int(input())
    apart_list = list(map(int, input().split()))
    view = 0
    for i in range(2, N + 2):
        new_list = apart_list[i-2:i+3]
        if max(new_list) == apart_list[i]:
            new_list = list(map(lambda x : apart_list[i] - x , new_list))
            new_list.pop(2)
            view += min(new_list)
        
    print(f'#{j + 1} {view}')

