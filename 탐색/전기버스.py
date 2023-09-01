# SWea 4831. 전기버스 

# T = int(input())

# for tc in range(1, T + 1):
    
#     K, N, M = map(int, input().split()) 
#     # K는 한번에 이동할 수 있는 정류장 개수, N은 종착점, M은 정류장 개수
    
#     bus_stop = list(map(int, input().split()))
#     bus_stop.append(N) # 마지막 도착지도 추가해줌

#     bus = 0     # 버스의 위치
#     b = 0       # 들린 정류장의 개수
#     for j in range(M):
#         if bus + K < bus_stop[j + 1] and bus + K >= bus_stop[j]: # 현재 버스의 위치가 두 정거장 사이에 있다면
#             bus = bus_stop[j] # 그 중 앞에 있는 곳에 들리고
#             b += 1  # 들린 정류장 개수 +1

#         if (bus_stop [j + 1] - bus_stop [j]) > K: # 근데 만약 인접한 두 정거장 사이의 거리가 간격보다 크다면
#             b = 0    # 정류장 개수 0으로 바꾸고
#             break   # 그만
#     print(f'#{tc} {b}')




# 강사님 코드

# T = int(input())

# for tc in range(1,T + 1):
#     K, N, M = map(int, input().split())
#     arr = list(map(int, input().split()))
#     ch = [0] * (N + 1)

#     for i in arr:
#         ch[i] += 1
    
#     current = 0     # 현재 위치
#     count = 0       # 충전 횟수
#     while current < N:
#         # 갈 수 있는 최대 거리 계산
#         if ch[current + K]:
#             current += K
#             count += 1
#         # 충전소 찾기(뒤에서부터)
#         else:
#             for j in range(1, K):
#                 # 충전소를 찾으면 충전하고, count 중가
#                 if ch[current + K - j]:
#                     current += K - j
#                     count += 1
#                     break
#             # 충전소가 없으면 0 출력, 반복 종료
#             else:
#                 count = 0
#                 break
#         # 최대거리가 도착점보다 멀거나 같으면, 반복 종료
#         if current + K >= N:
#             current = N
            
#     print(f'#{tc} {count}')




    
# 방법2) 0부터 시작해서 K만큼 더했을때, 처음으로 작은게 나오는걸 뒤에서부터 탐색

# T = int(input())

# for tc in range(1, T + 1):
#     K, N, M = map(int, input().split()) 
#     bus_stop = list(map(int, input().split()))
#     bus_stop.append(N)
#     bus = 0
#     b = 0
#     while bus <= N:
#         for j in range(M, -1, -1):
#             if bus + K >= bus_stop[j]:
#                 b += 1
#                 new_bus = bus_stop[j] #새로운 버스의 위치
#             else: 
#                 continue
#         bus = new_bus
        
#     print(b)


# # 전기버스 (수민언니)
# T = int(input())

# for tc in range(1, T + 1):
#     K, N, M = map(int, input().split())
#     stations = list(map(int, input().split()))
#     bus_stops = [0] * (N + 1)
#     cnt = 0
#     zeros = 1
#     total = 0
#     is_possible = True
#     for i in stations:
#         bus_stops[i] = 1
#     print(bus_stops)
#     # 종점에 도착할 수 없는 경우
#     for i in range(0, N):
#         if bus_stops[i] == bus_stops[i + 1] == 0:
#             zeros += 1
#             if zeros == K and (i + 1) != N and (i + 1) != (K - 1):
#                 is_possible = False
#         else:
#             zeros = 1

#     # 종점에 도착할 수 있는 경우
#     if is_possible:
#         current = 0
#         while current < N:
#             #print('loop를 시작합니다.')
#             if current + K >= N:
#                 break
#             elif bus_stops[current + K] == 1:
#                 #print(f'{K}칸 이동하니 충전소가 있네요.')
#                 current += K
#                 cnt += 1
#                 #print(f'현재 위치는 {current}입니다.')
#             else:
#                 for i in range(K - 1, 0, -1):
#                     if bus_stops[current + i] == 1:
#                         #print(f'{K}칸 내에서 가장 가까운 충전소입니다.')
#                         current += i
#                         cnt += 1
#                         #print(f'현재 위치는 {current}입니다.')
#                         break
#     if is_possible:
#         print(f'#{tc} {cnt}')
#     else:
#         print(f'#{tc}', 0)