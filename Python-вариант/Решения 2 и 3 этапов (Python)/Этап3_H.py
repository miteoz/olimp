MOD = 10 ** 9 + 7

def mul(A, B):
    return [[(A[i][0] * B[0][j] + A[i][1] * B[1][j]) % MOD for j in range(2)] for i in range(2)]

a, b, n = map(int, input().split())
if n == 1:
    print(a % MOD)
elif n == 2:
    print(b % MOD)
else:
    R = [[1, 0], [0, 1]]
    T = [[1, 1], [1, 0]]                              # (f_i, f_{i-1}) -> (f_{i+1}, f_i)
    p = n - 2
    while p:
        if p & 1:
            R = mul(R, T)
        T = mul(T, T)
        p >>= 1
    print((R[0][0] * b + R[0][1] * a) % MOD)
