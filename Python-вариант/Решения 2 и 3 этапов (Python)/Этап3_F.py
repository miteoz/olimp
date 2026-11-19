import sys
from bisect import bisect_left

def nearest(v, x):                                   # min |v[i] - x| в отсортированном v
    i = bisect_left(v, x)
    best = float('inf')
    if i < len(v):
        best = v[i] - x
    if i > 0 and x - v[i - 1] < best:
        best = x - v[i - 1]
    return best

def main():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    xs = sorted(int(data[1 + 2 * i]) for i in range(t))
    ys = sorted(int(data[2 + 2 * i]) for i in range(t))
    pos = 1 + 2 * t
    q = int(data[pos]); pos += 1
    res = []
    for i in range(q):
        x, y = int(data[pos]), int(data[pos + 1])
        pos += 2
        res.append(min(nearest(xs, x), nearest(ys, y)))
    print(' '.join(map(str, res)))

main()
