N = int(input())
nums = list(map(int,input().split()))
nums.sort()

# 홀수면
if N % 2:
  print(sum(nums[N//2 + 1:]) * 2 + nums[N//2])
# 짝수면
else:
  print(sum(nums[N//2:]) * 2)    