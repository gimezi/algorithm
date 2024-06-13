# 크로아티아 알파벳

p = 0
sentense = input()
alphabet = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0
while p < len(sentense):
    flag = False
    if p < len(sentense) - 2:
        if sentense[p] + sentense[p + 1] + sentense[p + 2] == 'dz=':
            flag = True
            cnt += 1
            p += 3
    if flag == False and p < len(sentense) - 1:
        if sentense[p] + sentense[p + 1] in alphabet:
            flag = True
            cnt += 1
            p += 2
    if flag == False:
        cnt += 1
        p += 1

print(cnt)