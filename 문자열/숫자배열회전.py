## SWea 숫자배열회전 D2


T =  int(input())

for tc in range(1, T + 1):
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]

    dir1 = []
    for j in range(N):
        a = []
        for i in range(N):
            a.append([N - i, j])
        dir1.append(a)

    dir2 = []
    for i in range(N):
        b = []
        for j in range(N):
            b.append([N - i, N - j])
        dir2.append(b)

    dir3 = []
    for j in range(N):
        c = []
        for i in range(N):
            c.append([i, N - j])
        dir3.append(c)

    print(dir1, dir2, dir3)

