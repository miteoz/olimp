import sys
import heapq

def main():
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])
    a = list(map(int, data[2:2 + n]))
    g = [[] for _ in range(n)]
    indeg = [0] * n
    pos = 2 + n
    for _ in range(m):
        u, v = int(data[pos]), int(data[pos + 1])
        pos += 2
        g[u].append(v)
        indeg[v] += 1
    heap = [(-a[v], v) for v in range(n) if indeg[v] == 0]   # минус — чтобы куча была max
    heapq.heapify(heap)
    res = []
    while heap:
        neg, v = heapq.heappop(heap)
        res.append(-neg)
        for u in g[v]:
            indeg[u] -= 1
            if indeg[u] == 0:
                heapq.heappush(heap, (-a[u], u))
    if len(res) < n:
        print("no solution")
    else:
        print(' '.join(map(str, res)))

main()
