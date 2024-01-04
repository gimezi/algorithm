# 4839 이진탐색

T = int(input())

def count_find(p, key):
    count = 0
    start = 1
    end = p
    while start <= end:
        middle = int((start + end) / 2)
        if middle == key:  
            return count
        elif middle > key:
            end = middle 
        else:
            start = middle
        count += 1 
    return 10000

for tc in range(1, T + 1):
    P, A, B = map(int, input().split())
    a_count = count_find(P, A)
    b_count = count_find(P, B)
    if a_count < b_count:
        winner = 'A'
    elif a_count > b_count:
        winner = 'B'
    else:
        winner = 0
    
    print(f'#{tc} {winner}')
    