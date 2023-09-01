# 24726번 미적분학 입문하기2
'''
주어진 삼각형을 x축으로 회전시켰을 때 나오는 회전체의 부피와 
y축으로 회전시켰을 때 나오는 회전체의 부피를 공백을 사이에 두고 출력한다.
'''


import math
def s(a, b, t):
    ans = (a ** 2) * (t ** 3) / 3 + a * b * (t ** 2) + (b ** 2) * t
    return ans

def inte(x1, y1, x2, y2):               # x1부터 x2까지 적분
    if x1 == x2:
        return 0
    a = (y1 - y2) / (x1 - x2)           # 기울기
    b = y1 - a * x1                     # y절편
    S = s(a, b, x2) - s(a, b, x1)
    return S * math.pi

a1, b1, a2, b2, a3, b3 = map(int,input().split())
coor = [(a1, b1), (a2, b2), (a3, b3)]

coor.sort()  # x좌표 기준으로 정렬
s1 = inte(coor[0][0], coor[0][1], coor[1][0], coor[1][1]) + inte(coor[1][0], coor[1][1], coor[2][0], coor[2][1])
s2 = inte(coor[0][0], coor[0][1], coor[2][0], coor[2][1])

result1 = abs(s1 - s2)

coor.sort(key= lambda x:x[1])   # y좌표 기준으로 정렬
s3 = inte(coor[0][1], coor[0][0], coor[1][1], coor[1][0]) + inte(coor[1][1], coor[1][0], coor[2][1], coor[2][0])
s4 = inte(coor[0][1], coor[0][0], coor[2][1], coor[2][0])

result2 = abs(s3 - s4)

print(result1, result2)