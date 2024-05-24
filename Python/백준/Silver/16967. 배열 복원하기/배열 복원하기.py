## 백준 배열 복원하기 16967번

'''
3 3 2 2 
1 2 3 0 0 
4 5 6 0 0 
7 8 10 2 3
0 0 4 5 6
0 0 7 8 9
'''

H, W, X, Y = map(int, input().split())
A1 = []
B1 = []
for i in range(H + X):
    tmp = list(map(int,input().split()))
    if i < H:
        A1.append(tmp[:W])
    if i >= X:
        B1.append(tmp[Y:])

ans = []
for i in range(H):
    if i < X:
        ans.append(A1[i])
    else:
        temp = []
        for j in range(W):
            if j < Y:
                temp.append(A1[i][j])
            else:
                temp.append(B1[i - X][j - Y] - ans[i - X][j - Y])
        ans.append(temp)


for i in range(H):
    print(*ans[i])
                
