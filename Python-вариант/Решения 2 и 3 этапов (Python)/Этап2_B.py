import sys

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    p = a.index(1)                                   # где стоит трек 1
    ok = all(a[(p + i) % n] == i + 1 for i in range(n))   # дальше по кругу 2, 3, ...
    print("Yes" if ok else "No")

main()
