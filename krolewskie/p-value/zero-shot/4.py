import numpy as np

def count_ones(n):
    return bin(n).count('1')

def find_kth_royal_number(k):
    count = 0
    i = 0
    while True:
        if count_ones(i) % 2 == 0:
            count += 1
            if count == k:
                return i
        i += 1

def main():
    t = int(input())
    for _ in range(t):
        k = int(input())
        result = find_kth_royal_number(k)
        print(result)

if __name__ == "__main__":
    main()
