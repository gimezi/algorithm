# 백준 1072번
'''
이분 탐색........


'''

X, Y = map(int,input().split())
Z = (Y * 100) // X

def check(n):
  if (Y + n) * 100 // (X + n) > Z:
    return True
  else:
    return False

def find(start, end):
  while start <= end:  # 여기에 start != end면 안되는데 왜 그런거지
    mid = (start + end) // 2
    if check(mid):
      end = mid - 1
    else:
      start = mid + 1
  return start

if Z >= 99:
  print(-1)
else:
  print(find(1, 10000000000))