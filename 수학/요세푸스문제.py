# 1158 요세푸스 문제

N, K = map(int, input().split())

lst = [i for i in range(1, N + 1)]
arr = []

i = K - 1
while len(lst) > 0:
    if i >= len(lst):
        i = i % len(lst)
    out = lst.pop(i)
    i += K - 1
    arr.append(out)

arr = list(map(str,arr))
print('<'+', '.join(arr)+'>')