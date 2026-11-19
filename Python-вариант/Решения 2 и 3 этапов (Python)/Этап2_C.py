import sys

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    best = None
    cur = 0
    for x in map(int, data[1:1 + n]):
        cur = x if cur + x < x else cur + x          # начать заново или продолжить
        if best is None or cur > best:
            best = cur
    print(best)

main()
