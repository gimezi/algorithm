# 7568번 덩치

N = int(input())
h = []
w = []
for _ in range(N):
    a, b = map(int,input().split())
    h.append(a)
    w.append(b)

score = []
for i in range(N):
    score.append([i, 0])

for i in range(N):
    for j in range(N):
        if i == j:
            pass
        else:
            if h[i] < h[j] and w[i] < w[j]:
                score[i][1] += 1

for i in range(N):
    print(score[i][1] + 1, end = ' ')



