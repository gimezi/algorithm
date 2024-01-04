def quick(arr, start, end):
    if start >= end:
        return 
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        # pivot보다 큰 값을 찾을때까지 왼쪽 포인터 이동
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        # pivot보다 작은 값을 찾을때까지 오른쪽 포인터 이동
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]

    quick(arr,start, right - 1)
    quick(arr, right + 1, end)  

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int,input().split()))
    quick(arr, 0, N - 1)
    print(f'#{tc} {arr[N//2]}')