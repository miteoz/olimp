import sys

def main():
    data = sys.stdin.buffer.read().split()
    n, k = int(data[0]), int(data[1])
    p = [0] + list(map(int, data[2:2 + n]))
    bit = [0] * (n + 1)

    def add(i, v):
        while i <= n:
            bit[i] += v
            i += i & -i

    def pref(i):
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s

    st = [1, 0, 0]                                   # окно [L, R] и число инверсий в нём

    def cost(l, r):                                  # инверсии на [l, r], указатели как в Мо
        L, R, inv = st
        while R < r:
            R += 1; inv += (R - L) - pref(p[R]); add(p[R], 1)
        while L > l:
            L -= 1; inv += pref(p[L] - 1); add(p[L], 1)
        while R > r:
            add(p[R], -1); inv -= (R - L) - pref(p[R]); R -= 1
        while L < l:
            add(p[L], -1); inv -= pref(p[L] - 1); L += 1
        st[0], st[1], st[2] = L, R, inv
        return inv

    INF = float('inf')
    prv = [INF] + [cost(1, i) for i in range(1, n + 1)]   # один отрезок
    for j in range(2, k + 1):
        cur = [INF] * (n + 1)
        stack = [(j, n, j - 1, n - 1)]               # «разделяй и властвуй» без рекурсии
        while stack:
            l, r, optl, optr = stack.pop()
            if l > r:
                continue
            m = (l + r) // 2
            best, bi = INF, optl
            for t in range(optl, min(m - 1, optr) + 1):
                if prv[t] == INF:
                    continue
                v = prv[t] + cost(t + 1, m)
                if v < best:
                    best, bi = v, t
            cur[m] = best
            stack.append((m + 1, r, bi, optr))
            stack.append((l, m - 1, optl, bi))
        prv = cur
    print(prv[n])

main()
