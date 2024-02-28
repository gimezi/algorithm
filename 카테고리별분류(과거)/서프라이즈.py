# 서프라이즈

N = int(input())
arr = list(map(int,input().split()))

# 차이의 최소값
minval = float('inf')
# 정답이 될 합의 최대값
result = 0

# 중심을 1부터끝까지 돌려줌
for i in range(N - 1):
  left = i
  right = i + 1
  # 처음 합을 하나씩만 해주고 비교하면서 더해줌
  left_sum = arr[left]
  right_sum = arr[right]
  while True:
    # 현재 차이
    diff = abs(left_sum - right_sum)
    # 만약 지금이 최소값이라면
    if diff == minval:
      result = max(result, left_sum + right_sum)
    # 기존의 최소값보다 더 작다면
    elif diff < minval:
      minval = diff
      result = left_sum + right_sum

    # 왼쪽이 더 크다면, 오른쪽에 합세해줌
    if left_sum > right_sum:
      # 근데 만약 제일 끝이라면? -> 다음꺼
      if right == N - 1:
        break
      right += 1
      right_sum += arr[right]
    # 오른쪽이 더 크다면, 왼쪽에 더해주기
    elif right_sum > left_sum:
      if left == 0:
        break
      left -= 1
      left_sum += arr[left]
    # 같다면
    else:
      # 그 중에서도 만약 둘디 끝이라면
      if left == 0 or right == N - 1:
        break
      left -= 1
      right += 1
      left_sum += arr[left]
      right_sum += arr[right]

print(result)