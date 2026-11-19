import sys

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    b = list(map(int, data[1 + n:1 + 2 * n]))
    c = list(map(int, data[1 + 2 * n:1 + 3 * n]))
    cost = [(a[i], b[i], c[i]) for i in range(n)]    # cost[i][k]: раньше вышли k соседей
    INF = float('inf')
    # o = 1, если правый сосед (i+1) опубликован РАНЬШЕ трека i
    dp = [cost[0][0], cost[0][1] if n > 1 else INF]
    for i in range(1, n):
        nd = [INF, INF]
        for o in range(2):
            if i == n - 1 and o == 1:
                continue                             # у последнего нет правого соседа
            for p in range(2):                       # p == 0: трек i-1 вышел раньше i
                if dp[p] == INF:
                    continue
                val = dp[p] + cost[i][(p == 0) + o]
                if val < nd[o]:
                    nd[o] = val
        dp = nd
    print(dp[0])

main()
