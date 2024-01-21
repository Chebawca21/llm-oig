import numpy as np

def find_kth_royal_number(k):
    binary_representation = bin(2)[2:]  # Initial binary representation for decimal 2
    count_ones = binary_representation.count('1')

    while count_ones % 2 != 0:
        k += 1
        binary_representation = bin(k)[2:]
        count_ones = binary_representation.count('1')

    return k

def main():
    t = int(input())  # Number of queries

    for _ in range(t):
        ki = int(input())  # k-th royal number query
        result = find_kth_royal_number(ki)
        print(result)

if __name__ == "__main__":
    main()
