import sys
from collections import deque

def main():
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])
    N = n * m
    # до двух меток на клетку: (источник, расстояние) от РАЗНЫХ источников
    s1 = [-1] * N; d1 = [0] * N
    s2 = [-1] * N; d2 = [0] * N
    q = deque()
    for i in range(N):
        if data[2 + i] == b'1':
            s1[i] = i
            q.append(i * 2)                          # клетка*2 + номер метки
    while q:
        e = q.popleft()
        v, k = e >> 1, e & 1
        if k:
            src, dist = s2[v], d2[v] + 1
        else:
            src, dist = s1[v], d1[v] + 1
        x, y = divmod(v, m)
        for u in ((v - m) if x > 0 else -1, (v + m) if x + 1 < n else -1,
                  (v - 1) if y > 0 else -1, (v + 1) if y + 1 < m else -1):
            if u < 0:
                continue
            if s1[u] == -1:
                s1[u] = src; d1[u] = dist; q.append(u * 2)
            elif s2[u] == -1 and s1[u] != src:
                s2[u] = src; d2[u] = dist; q.append(u * 2 + 1)
    out = []
    for x in range(n):
        row = []
        for y in range(x * m, x * m + m):
            row.append(d2[y] if s1[y] == y else d1[y])   # заряженная: ближайший ДРУГОЙ
        out.append(' '.join(map(str, row)))
    sys.stdout.write('\n'.join(out) + '\n')

main()
