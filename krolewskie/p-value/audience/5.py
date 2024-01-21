import numpy as np

def count_ones(n):
    return bin(n).count('1')

def find_kth_royal_number(k):
    current_number = 0
    while True:
        if count_ones(current_number) % 2 == 0:
            k -= 1
            if k == 0:
                return current_number
        current_number += 1

def main():
    t = int(input())
    for _ in range(t):
        k = int(input())
        result = find_kth_royal_number(k)
        print(result)

if __name__ == "__main__":
    main()
