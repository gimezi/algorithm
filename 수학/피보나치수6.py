# 11444번 피보나치 수3

def matmulti(mat1, mat2):
    result = [[0, 0], [0, 0]]
    result[0][0] = (mat1[0][0]*mat2[0][0]%mod) + (mat1[0][1]*mat2[1][0]%mod)%mod
    result[0][1] = (mat1[0][0]*mat2[1][0]%mod) + (mat1[0][1]*mat2[1][1]%mod)%mod
    result[1][0] = (mat1[1][0]*mat2[0][0]%mod) + (mat1[1][1]*mat2[1][0]%mod)%mod
    result[1][1] = (mat1[1][0]*mat2[1][0]%mod) + (mat1[1][1]*mat2[1][1]%mod)%mod
    return result

mat = [[0, 1], [1, 1]]
mod = int((1e+9)+7)

def f(mat, n):
    if n == 0:
        return [[1, 0], [0, 1]]
    if n % 2:
        mat1 = f(mat, (n - 1) // 2)
        return matmulti(matmulti(mat1, mat1), mat)
    else:
        mat2 = f(mat, n // 2)
        return matmulti(mat2, mat2)
N = int(input())
print(f(mat, N)[0][1] % mod)