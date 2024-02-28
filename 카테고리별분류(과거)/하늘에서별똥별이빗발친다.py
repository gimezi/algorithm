# 하늘에서 별똥별이 빗발친다

N, M, L, K = map(int,input().split())
stars = []
for _ in range(K):
  a, b = map(int, input().split())
  stars.append((a, b))

# x 기준으로 정렬
stars.sort()

ans = 1

for i in range(K - 1):
  temp = [stars[i]]
  for j in range(i + 1, K):
    if stars[j][0] <= stars[i][0] + L:
      temp.append(stars[j])
  # 이걸 다시 y기준으로 정렬해서
  temp.sort(key=lambda x: x[1])
  maxcnt = 1
  for p in range(len(temp) - 1):
    cnt = 1
    for q in range(p + 1, len(temp)):
      if temp[q][1] <= temp[p][1] + L:
        cnt += 1
    if cnt > maxcnt:
      maxcnt = cnt
  if maxcnt > ans:
    ans = maxcnt
print(K - ans)