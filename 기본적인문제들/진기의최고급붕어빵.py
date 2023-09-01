# 진기의 최고급 붕어빵

'''
그래서 오늘은 N명의 사람이 자격을 얻었다.
진기는 0초부터 붕어빵을 만들기 시작하며, M초의 시간을 들이면 K개의 붕어빵을 만들 수 있다.
서빙은 진기가 하는 것이 아니기 때문에, 
붕어빵이 완성되면 어떤 시간 지연도 없이 다음 붕어빵 만들기를 시작할 수 있다.
0초 이후에 손님들이 언제 도착하는지 주어지면, 
모든 손님들에게 기다리는 시간없이 붕어빵을 제공할 수 있는지 판별하는 프로그램을 작성하라.
4
2 2 2
3 4
2 2 2
1 2
2 2 1
4 2
2 2 1
3 2


#1 Possible
#2 Impossible
#3 Possible
#4 Impossible

'''

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    result = 'Possible'
    for i in range(N):
        if i + 1 > arr[i] // M * K:
            result = 'Impossible'
            break
    print(f'#{tc} {result}')




















# 너무 직관적으로 했더니 시간초과가 나버림
T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int,input().split())
    time = list(map(int,input().split()))
    time.sort()
    # 우선 붕어빵 만들어
    is_true = True
    bong = [0 for _ in range(12000)]
    a = M
    while a < len(bong):
        for i in range(a, len(bong)):
            bong[i] += K
        a += M
    for t in time:
        if bong[t] >= 1:
            for i in range(t, len(bong)):
                bong[i] -= 1
        else:
            is_true = False
            break
    if is_true:
        print(f'#{tc} Possible')
    else:
        print(f'#{tc} Impossible')