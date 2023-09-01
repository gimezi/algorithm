# SWEA 피자굽기
'''
N개의 피자를 동시에 구울 수 있는 화덕이 있다.
피자는 치즈가 모두 녹으면 화덕에서 꺼내며, 치즈의 양은 피자마다 다르다.
1번부터 M번까지 M개의 피자를 순서대로 화덕에 넣을 때, 
치즈의 양에 따라 녹는 시간이 다르기 때문에 꺼내지는 순서는 바뀔 수 있다.
주어진 조건에 따라 피자를 구울 때, 
화덕에 가장 마지막까지 남아있는 피자 번호를 알아내는 프로그램을 작성하시오.

[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄부터 테스트 케이스의 첫 줄에 화덕의 크기 N과 피자 개수 M이 주어지고, 
다음 줄에 M개의 피자에 뿌려진 치즈의 양을 나타내는 Ci가 주어진다.
3<=N<=20, N<=M<=100, 1<=Ci<=20

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 번호를 출력한다.

[input]
3
3 5
7 2 6 5 3
5 10
5 9 3 9 9 2 5 8 7 1
5 10
20 4 5 7 3 15 2 1 2 2

[output]
#1 4
#2 8
#3 6
'''

from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int,input().split()))
    lst = []                           # lst안에 idx도 같이 넣어줌 
    que = deque()
    for i in range(M):              
        lst.append([arr[i], i + 1])    # lst = [[5, 4], [3, 5]]
    for _ in range(N):
        que.append(lst.pop(0))         # que = deque([[7, 1], [2, 2], [6, 3]])

    while len(que) > 1:
        a_set = que.popleft()
        a_set[0] = a_set[0] // 2       # que의 맨앞에 꺼 빼와서 2로 나눠줌
        if a_set[0]:                   # 0이 아니면
            que.append(a_set)
        else:                          # 0이라면
            if lst: 
              que.append(lst.pop(0))     # lst에서 앞에꺼 가져옴
            else:
                pass
    result = que[0][1]
    print(f'#{tc} {result}')
        
























# from collections import deque
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int,input().split())
#     arr = list(map(int, input().split()))
#     oven = deque(arr[:N])
#     print(arr[N - 1])
#     remain = arr[N:]

#     for i in range(M - N):
#         oven.append(0)
    
#     def pizza():
#         cnt = 0
#         while True:
#             print(oven)
#             print(cnt)
            
#             for i in range(M):
#                 if sum(oven) == 1 and oven[i]:
#                     return i
#                 if oven[i]:
#                     n = oven[i] // 2
#                     if n:
#                         oven[i] = n
#                     else:
#                         cnt += 1
#                         oven[i] = 0
#                         idx = N + cnt -1 
#                         if idx < M:
#                             oven[N + cnt - 1] = remain.pop(0)

#     print(pizza())
                    

#     # print(oven)