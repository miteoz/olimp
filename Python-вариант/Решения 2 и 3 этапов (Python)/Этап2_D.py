import sys

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    total = [0] * 7                                  # total[d] — сумма, если общий день d
    pos = 1
    for _ in range(n):
        row = list(map(int, data[pos:pos + 7]))
        pos += 7
        v0, v1, v2 = sorted(row)[:3]                 # три самых маленьких значения
        s3 = v0 + v1 + v2
        for d in range(7):
            # если a[d] среди трёх минимальных — берём ровно эти три дня,
            # иначе день d плюс два самых дешёвых
            total[d] += s3 if row[d] <= v2 else row[d] + v0 + v1
    print(min(total))

main()
