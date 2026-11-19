import sys

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    p = [0] + list(map(int, data[1:1 + n]))
    used = bytearray(n + 1)
    cycles = 0
    for i in range(1, n + 1):
        if not used[i]:
            cycles += 1
            j = i
            while not used[j]:                       # обходим цикл i -> p[i] -> ...
                used[j] = 1
                j = p[j]
    print(n - cycles)

main()
