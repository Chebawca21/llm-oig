import numpy as np

def count_set_bits(num):
    # Count the number of set bits (1s) in the binary representation of the number
    return bin(num).count('1')

def find_kth_royal_number(k):
    # Find the k-th royal number
    royal_number = 0
    while True:
        if count_set_bits(royal_number) % 2 == 0:
            k -= 1
        if k == 0:
            return royal_number
        royal_number += 1

def main():
    t = int(input())
    for _ in range(t):
        k = int(input())
        royal_number = find_kth_royal_number(k)
        print(royal_number)

if __name__ == "__main__":
    main()
