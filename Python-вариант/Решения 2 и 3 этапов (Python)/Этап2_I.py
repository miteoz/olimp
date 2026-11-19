import sys

def main():
    data = sys.stdin.buffer.read().split()
    n, x = int(data[0]), int(data[1])
    a = sorted(set(map(int, data[2:2 + n])))
    MOD = 10 ** 9 + 7
    dp = [0] * (x + 1)
    dp[0] = 1                                        # пустой плейлист
    for s in range(1, x + 1):
        total = 0
        for v in a:
            if v > s:
                break
            total += dp[s - v]                       # последний трек длительности v
        dp[s] = total % MOD
    print(dp[x])

main()
