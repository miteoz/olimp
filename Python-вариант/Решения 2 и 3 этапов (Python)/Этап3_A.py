n, k = map(int, input().split())
m = n // k                                           # сколько кратных k среди 1..n
print(n * (n + 1) // 2 - k * (m * (m + 1) // 2))
