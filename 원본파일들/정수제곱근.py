n = int(input())

start = 0
end = 2 ** 32

while start <= end:
  mid = (start + end) // 2
  if mid * mid < n:
    start = mid + 1
  else:
    end = mid - 1

print(start)