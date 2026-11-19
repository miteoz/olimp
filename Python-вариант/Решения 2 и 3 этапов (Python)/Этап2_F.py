n, k = map(int, input().split())
if n <= 1 or k == 0:
    print(0)
else:
    p = k.bit_length() - 1                           # старший бит k
    print((n - 1) * ((1 << (p + 1)) - 1))            # чередуем 2^p и 2^p - 1
