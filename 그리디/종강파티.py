# 종강파티 - 그리디

'''
오늘은 드디어 1학기가 끝나는 날이다. 그렇기에 코코는 친구들과 함께 바람직하게 취할 준비를 하고 있다.
종강 파티에는 N명의 친구들이 참석할 예정이다. 
모두 거하게 취하기 위해 한명당 보드카 한병씩을 준비하려고 한다.
여러마트에서 보드카는 6병 세트, 또는 낱개로 팔고 있다. 물론 마트마다 각 제품의 가격은 상이하다.
아직 학생인 코코는 당연히 최대한 적은 돈을 써서 파티를 준비하려고 한다.
참석 인원 N과 M개의 마트에서 파는 제품의 정보가 주어졌을 때, 
1인당 최소 하나 이상의 보드카 준비하기 위해서 최소 얼마를 사용해야 하는지를 구하시오.

[입력]
첫번째 줄에 참석 인원 N과 마트의 개수 M이 주어진다. (1 <= N <= 100, 1 <= M <= 50)
두번째 줄부터 M개의 줄에 걸처 각 마트에서 판매하는 보드카의 6병 세트와 낱개의 가격이 
공백으로 구분되어 주어진다. (0 <= 가격 <= 1,000)

10 2
5 2
4 3

[출력]
첫번째 줄에 1인당 1보드카를 준비하기 위해 필요한 최소 비용을 출력한다.

8

'''

N, M = map(int,input().split())
sixarr = []
onearr = []
for _ in range(M):
    a, b = map(int,input().split())
    sixarr.append(a)
    onearr.append(b)

minsix = min(sixarr)
minone = min(onearr)

if minsix < minone * 6:
    rem = N % 6
    six = N // 6
    if rem * minone > minsix:
        result = minsix * (six + 1)
    else:
        result = minone * rem + minsix * six
else:
    result = minone * N

print(result)