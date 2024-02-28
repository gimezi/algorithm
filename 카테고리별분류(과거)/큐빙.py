# 큐빙 
'''
큐브를 돌려보자
4
1
L-
2
F+ B+
4
U- D- L+ R+
10
L- U- L+ U- L- U- U- L+ U+ U+

가장 윗면만 나오면 댐
'''

# 현재 상태 상, 하, 앞, 뒤, 좌, 우
cube = [
  ['wwk', 'www', 'www'], ['yyy','yyy','yyy'],
  ['rrr','rrr','rrr'], ['ooo','ooo','ooo'],
  ['ggg','ggg','ggg'], ['bbb','bbb','bbb']
]

# 해당하는 면을 돌려주는 함수
# side는 돌려질 면, N은 몇번 돌릴껀지(1번은 시계, 3번은 반시계임)
def SideSpin(side):
  newside = [[], [], []]
  newside[0] = [side[2][0], side[1][0], side[0][0]]
  newside[1] = [side[2][1], side[1][1], side[0][1]]
  newside[2] = [side[2][2], side[1][2], side[0][2]]
  side = newside
  return side

# 돌려보자, now는 현재 상태, N은 몇번인지
def TurnTop(now, N):
  for _ in range(N):
    next_cube = [[],[],[]]
    SideSpin(now[0], 1)