# 셀프넘버

def make_num(n):
    new = n
    while True:
        if n // 10 >= 1:
            new += n % 10 
            n = n // 10
        else:
            new += n
            break
    return new

dic = [0 for _ in range(10001)]
dic[0] = 1
for i in range(1, 10001):
    next_num = make_num(i)
    if next_num <= 10000:
        dic[next_num] = 1

for i in range(10001):
    if dic[i] == 0:
        print(i)
