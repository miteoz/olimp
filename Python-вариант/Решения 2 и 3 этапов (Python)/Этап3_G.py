import sys
from collections import deque

def main():
    lines = sys.stdin.read().split('\n')
    n = int(lines[0])
    key, text = [], []
    for i in range(1, n + 1):
        line = lines[i].rstrip('\r')
        k, t = line.split(':', 1)                    # делим по ПЕРВОМУ двоеточию
        key.append(k)
        text.append(t)
    idx = {k: i for i, k in enumerate(key)}
    g = [[] for _ in range(n)]
    rg = [[] for _ in range(n)]
    target = [True] * n
    for i in range(n):
        seen = set()
        for w in text[i].split():                    # split() сам съедает лишние пробелы
            v = idx.get(w)
            if v is None:
                continue
            target[i] = False                        # есть ключ (даже свой) — не целевая
            if v != i and v not in seen:
                seen.add(v)
                g[i].append(v)
                rg[v].append(i)
    # BFS от всех целевых по обратным рёбрам
    dist = [-1] * n
    q = deque()
    for i in range(n):
        if target[i]:
            dist[i] = 0
            q.append(i)
    while q:
        v = q.popleft()
        for u in rg[v]:
            if dist[u] == -1:
                dist[u] = dist[v] + 1
                q.append(u)
    if dist[0] == -1:
        print("no solution")
        return
    path = [0]
    v = 0
    while dist[v] > 0:                               # жадно: минимальный ключ на каждом шаге
        v = min((u for u in g[v] if dist[u] == dist[v] - 1), key=lambda u: key[u])
        path.append(v)
    print(' '.join(key[u] for u in path))
    print(text[v].strip())

main()
