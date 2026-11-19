import sys

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    first = {0: -1}                                  # баланс 0 «до начала» массива
    bal = best = 0
    for i in range(n):
        bal += 1 if int(data[1 + i]) % 2 == 0 else -1
        if bal in first:
            if i - first[bal] > best:
                best = i - first[bal]
        else:
            first[bal] = i
    print(best)

main()
