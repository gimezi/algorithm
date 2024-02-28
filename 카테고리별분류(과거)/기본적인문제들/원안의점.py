# 원 안의 점
T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    node = 0
    for i in range(1, n):
        for j in range(1, n):
            if i**2 + j ** 2 <= n ** 2:
                node += 1
    print(f'#{tc} {node * 4 + 4 * n + 1}')