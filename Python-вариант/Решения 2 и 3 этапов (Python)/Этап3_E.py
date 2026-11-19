import sys
from bisect import bisect_left

def main():
    data = sys.stdin.buffer.read().split()
    n, k = int(data[0]), int(data[1])
    a = sorted(map(int, data[2:2 + n]))

    def count(d):                                    # сколько пар с разностью <= d
        c = 0
        for j in range(n):
            c += j - bisect_left(a, a[j] - d, 0, j)
        return c

    lo, hi = -1, a[-1] - a[0]                         # count(lo) < k <= count(hi)
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if count(mid) >= k:
            hi = mid
        else:
            lo = mid
    print(hi)

main()
