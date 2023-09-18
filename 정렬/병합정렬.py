#분할함수(재귀) + 병합함수

#분할함수
def divide(arr):
    if len(arr) <= 1: #리스트의 길이가 1이하면 그대로 반환
        return arr
    middle = len(arr) // 2
    left = divide(arr[:middle]) #왼쪽부분
    right = divide(arr[middle:]) #오른쪽부분
    return merge(left, right) #나눈 두 부분을 병합

#병합 함수
def merge(left, right):
    global ans
    #왼쪽 리스트의 마지막 원소가 오른쪽 리스트의 마지막 원소보다 큰경우 answer 1 증가
    if right[-1] < left[-1]:
        ans += 1
    result = [] #병합 결과
    len_l = len(left)
    len_r = len(right)
    l = r = 0
    while l < len_l or r < len_r:
        #1. 왼쪽과 오른쪽 리스트 모두 남아 있는경우
        if l < len_l and r < len_r:
            if left[l] <= right[r]:
                result.append(left[l]) #왼쪽의 원소를 result에 추가
                l += 1
            else:
                result.append(right[r]) #오른쪽의 원소를 result에 추가
                r += 1
        #2. 오른쪽 리스트만 남아있는 경우
        elif l < len_l:
            result.append(left[l])
            l += 1
        #3. 왼쪽 리스트만 남아 있는 경우
        elif r < len_r:
            result.append(right[r])
            r += 1
    return result

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    result = divide(arr) #병합 정렬 실행
    print(f'#{tc} {result[N//2]} {ans}')








# def add(arr1, arr2):
#     global cnt1, cnt2
#     p = k = 0
#     lst = []
#     print(arr1, arr2)
#     if arr1[-1] < arr2[-1]:
#         cnt1 += 1
#     elif arr1[-1] > arr2[-1]:
#         cnt2 += 1
#     print(cnt1, cnt2)

#     while p < len(arr1) and k < len(arr2):
#         if arr1[p] < arr2[k]:
#             lst.append(arr1[p])
#             p += 1
#         elif arr1[p] == arr2[k]:
#             lst.append(arr1[p])
#             p += 1
#         else:
#             lst.append(arr2[k])
#             k += 1
#     if p != len(arr1):
#         while p < len(arr1):
#             lst.append(arr1[p])
#             p += 1
#     elif k != len(arr2):
#         while k < len(arr2):
#             lst.append(arr2[k])
#             k += 1
#     return lst


# def merge_sort(arr, N):
#     global cnt1, cnt2
#     i = 0
#     n_arr = []
#     if len(arr) == 1:
#         return
#     while i < N:
#         if i == N - 3:
#             add(arr[i], arr[i + 1] + arr[i + 2])
#             n_arr.append(arr[i] + arr[i + 1] + arr[i + 2])
#             break
#         else:
#             add(arr[i], arr[i + 1])
#             i += 2
#             n_arr.append(arr[i] + arr[i + 1])
#     print(n_arr)
#     return merge_sort(n_arr, len(n_arr))
    

# T = int(input())

# for tc in range(1, T + 1):
#     N = int(input())
#     arr1 = list(map(int, input().split()))
#     arr = []
#     for num in arr1:
#         arr.append([num])
#     cnt1 = 0
#     cnt2 = 0
#     print(merge_sort(arr, N))
#     print(cnt1, cnt2)
    
