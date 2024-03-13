# 백준 1072번
'''
게임을 하면 X도 +1이 되는구나
Y도 +1이 되고
매번 계산을 하면 분명 시간초과가 날거같은데
'''

X, Y = map(int,input().split())
Z = (Y * 100) // X

def check(n):
  if (Y + n) * 100 // (X + n) > Z:
    return True
  else:
    return False

def find(start, end):
  while start <= end:
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