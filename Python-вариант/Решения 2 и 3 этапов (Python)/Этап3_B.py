import sys

def main():
    data = sys.stdin.buffer.read().split()
    n, x = int(data[0]), int(data[1])
    a = list(map(int, data[2:2 + n]))
    # пересечение [max - x, min + x] непусто  <=>  max - min <= 2x
    print("YES" if max(a) - min(a) <= 2 * x else "NO")

main()
